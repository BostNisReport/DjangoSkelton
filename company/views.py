# -*- coding: utf-8 -*-
import json
import datetime
import decimal

from django.utils.translation import ugettext as _
from constance import config
from django import forms
from django.utils import translation, timezone
from django.contrib.auth.forms import SetPasswordForm
from django.utils.translation import check_for_language
from django.contrib.auth import login, authenticate
from django.views.generic.base import TemplateView, RedirectView, View
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.contrib.auth.forms import PasswordResetForm

from .models import User
from .mixins import AjaxableResponseMixin
from .forms import ImageUploadForm

__all__ = ['HomeView']


def get_param(request, param):
    val = request.GET.get(param)

    if val is None:
        val = request.COOKIES.get('cur_'+param)

    return val


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self):
        ctx = super(HomeView, self).get_context_data()
        ctx['countries'] = []  # Warehouse.get_available_countries()
        ctx['region'] = []
        ctx['sizes'] = []  # CompanySize.objects.all()
        return ctx


class SignupView(TemplateView):
    template_name = 'signup.html'


class SigninView(TemplateView):
    template_name = 'login.html'


class AccountView(LoginRequiredMixin, TemplateView):
    login_url = '/signin/'
    template_name = 'account.html'

    def get_context_data(self):
        ctx = super(AccountView, self).get_context_data()
        # stripe.actions.customers.sync_customer(self.request.user.customer)
        # ctx['address_list'] = self.request.user.address_set.filter(is_deleted=False)
        # ctx['payment_list'] = self.request.user.customer.card_set.all()
        return ctx


class ApiEmailValidationView(AjaxableResponseMixin, View):
    def get(self, request, *args, **kwargs):
        email = request.GET.get('email')
        valid = False
        if email:
            if request.user:
                valid = not User.objects.filter(email__iexact=email).exclude(pk=request.user.pk).exists()
            else:
                valid = not User.objects.filter(email__iexact=email).exists()

        if valid:
            return self.render_to_json_response({
                'success': 'OK',
            })
        else:
            return self.render_to_json_response({
                'message': _('User with this email already exists'),
            })


class ResetPassword(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New password"),
                                    widget=forms.PasswordInput, min_length=6, max_length=100)
    new_password2 = forms.CharField(label=_("New password confirmation"),
                                    widget=forms.PasswordInput, min_length=6, max_length=100)


class ApiResetView(AjaxableResponseMixin, View):
    http_method_names = ['post', ]

    def post(self, request, *args, **kwargs):
        context = {}

        form = PasswordResetForm(request.POST)
        if form.is_valid():
            opts = {
                'request': request,
                'use_https': request.is_secure(),
                'from_email': settings.DEFAULT_FROM_EMAIL,
                'email_template_name': 'emails/forget/generate_link.html',
                'subject_template_name': 'emails/forget/reset_subject.txt',
                'html_email_template_name': 'emails/forget/generate_link.html',
            }
            form.save(**opts)

            context['success'] = True
            context['redirect_to'] = str(reverse_lazy('home'))
            return self.render_to_json_response(context)
        else:
            # Return an 'invalid login' error message.
            context['success'] = False
            context['error_msg'] = _('Invalid username.')

        return self.render_to_json_response(context)


class ApiLoginView(AjaxableResponseMixin, View):
    http_method_names = ['post', ]

    def post(self, *args, **kwargs):
        context = {}
        email = self.request.POST['email']
        password = self.request.POST['password']
        username = ""

        try:
            u = User.objects.get(email=email)
            username = u.username
        except:
            pass

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                context['success'] = True
                context['redirect_to'] = str(reverse_lazy('home'))
                return self.render_to_json_response(context)
            else:
                # Return a 'disabled account' error message
                context['success'] = False
                context['error_msg'] = _('User account has been disabled.')
        else:
            # Return an 'invalid login' error message.
            context['success'] = False
            context['error_msg'] = _('Invalid username/password.')

        return self.render_to_json_response(context)


class ApiRegisterView(AjaxableResponseMixin, View):
    http_method_names = ['post', ]

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        phone = request.POST.get('phone', None)
        msg = ""

        user = request.user
        can_register = False
        if user.is_authenticated():
            can_register = False
            msg = _('You are already registered')
        elif User.objects.filter(username=email).exists():
            msg = _('User with this email already exists')
        else:
            user = User(username=email)
            can_register = True
        if can_register:
            if phone and email and password:
                user.email = email
                user.phone = phone
                user.set_password(password)
                user.save()

                user = authenticate(username=user.username, password=password)
                login(self.request, user)
                return self.render_to_json_response({
                    'success': True,
                    'redirect_to': str(reverse_lazy('home'))
                })
            else:
                msg = _('Not all required field were filled')
        return self.render_to_json_response({
            'success': False,
            'error_msg': msg
        })


class ApiUpdateUserView(AjaxableResponseMixin, View):
    http_method_names = ['post', ]
    def post(self, request, *args, **kwargs):
        try:
            user = request.user
            msg = []

            email = request.POST.get('email')
            phone = request.POST.get('phone')
            pass1 = request.POST.get('password1')
            pass2 = request.POST.get('password2')

            if email is not None and user.email != email:
                user.email = email
                msg.append(_("Email was updated"))

            if phone is not None and user.phone != phone:
                user.phone = phone
                msg.append(_("Phone was updated"))

            if pass1 is not None and pass2 is not None and pass1 == pass2:
                user.set_password(pass1)
                msg.append(_("Password was updated"))

            user.save()

            return self.render_to_json_response({'success': True, 'msg': '<br>'.join(msg)})
        except:
            pass

        return self.render_to_json_response({'success': False, })


class ApiUpdatePhotoView(AjaxableResponseMixin, View):
    http_method_names = ['post', ]
    def post(self, request, *args, **kwargs):
        try:
            user = request.user
            msg = []

            form = ImageUploadForm(request.POST, request.FILES)
            if form.is_valid():
                user.photo = form.cleaned_data['image']
                msg.append(_("Photo was updated"))
                user.save()

            return self.render_to_json_response({'success': True, 'msg': '<br>'.join(msg)})
        except Exception as error:
            print("------------ %s " % error)
            pass

        return self.render_to_json_response({'success': False, })


class ChangeLocaleView(RedirectView):
    url = "/"
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        url = "/"
        try:
            url = self.request.META['HTTP_REFERER']
        except:
            pass

        return url

    def get(self, request, locale_code, *args, **kwargs):
        response = super(ChangeLocaleView, self).get(request, args, *kwargs)
        if locale_code and check_for_language(locale_code):
            translation.activate(locale_code)
            if hasattr(request, 'session'):
                request.session['django_language'] = locale_code
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, locale_code)
            translation.activate(locale_code)
        return response
