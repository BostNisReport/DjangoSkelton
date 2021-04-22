# -*- coding: utf-8 -*-
import datetime

from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.db import models
from django.conf import settings
from django.utils.crypto import get_random_string
from django.utils.timezone import utc
from django.contrib.auth.models import AbstractUser
from django.db.models import signals as signals
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save


from .utils import str_trunc, PathAndRename, ModelDiffMixin

__all__ = ['User']

AbstractUser._meta.get_field('username').max_length = 128
AbstractUser._meta.get_field('first_name').max_length = 128
AbstractUser._meta.get_field('last_name').max_length = 128
AbstractUser._meta.get_field('email').max_length = 128

# Abstract

class TimeStampedModel(models.Model):
    date_added = models.DateTimeField(auto_now_add=True, db_index=True)
    date_updated = models.DateTimeField(auto_now=True, db_index=True)

    class Meta(object):
        abstract = True


# User

class User(AbstractUser):
    phone = models.CharField(max_length=16, default='', blank=True)
    photo = models.ImageField(default=None, null=True, blank=True)


# class CompanyPhoto(TimeStampedModel):
#     company = models.ForeignKey(Company, related_name='photos')
#     photo = models.ImageField(upload_to=PathAndRename('company'))


