# -*- coding: utf-8 -*-
# from django.contrib.admin.options import StackedInline
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib import admin
from django import forms
from reversion.admin import VersionAdmin

from .models import User

@admin.register(User)
class UserAdmin(VersionAdmin, UserAdmin):
    pass


# StackedInline.sortable_field_name = ''  # fix for grapelli sortable_field_name error
# admin.TabularInline.sortable_field_name = ''  # fix for grapelli sortable_field_name error
