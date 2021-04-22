# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse_lazy

from .views import (HomeView, ResetPassword, SignupView, SigninView, AccountView,
                    ApiRegisterView, ApiEmailValidationView, ApiLoginView, ApiResetView, 
                    ApiUpdateUserView, ApiUpdatePhotoView)

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^account/$', AccountView.as_view(), name='account'),
    url(r'^signup/$', SignupView.as_view(), name='signup'),
    url(r'^signin/$', SigninView.as_view(), name='signin'),
    url(r'^logout/$', auth_views.logout, {'next_page': settings.LOGOUT_URL}, name="logout"),
    # url(r'^change-locale/(?P<locale_code>[\w-]+)/$', ChangeLocaleView.as_view(), name='change_locale'),

    url(r'^api/login/$', ApiLoginView.as_view(), name='login'),
    url(r'^api/reset/$', ApiResetView.as_view(), name='api_reset'),
    url(r'^api/register/$', ApiRegisterView.as_view(), name='register'),
    url(r'^api/email-validation/$', ApiEmailValidationView.as_view(), name='email_validation'),
    url(r'^api/update_user/$', ApiUpdateUserView.as_view(), name='update_user'),
    url(r'^api/update_photo/$', ApiUpdatePhotoView.as_view(), name='update_photo'),

    # 3 reset password
    url(r'^reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        auth_views.password_reset_confirm,
        {
            'template_name': 'new_password.html',
            'set_password_form': ResetPassword,
            'post_reset_redirect': reverse_lazy('reset_password_complete')
        },
        name='reset_password'),

    # 4 already reset
    url(r'^reset/done/$', auth_views.password_reset_complete,
        {'template_name': 'already_reset.html'},
        name='reset_password_complete'),
]

