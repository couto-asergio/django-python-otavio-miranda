# coding=utf-8

from django.db import models


# Class Abstract
class Base(models.Model):
    is_staff = models.BooleanField('Time', default=False)
    is_active = models.BooleanField('Active', default=True)
    date_joined = models.DateTimeField('Entry date', auto_now_add=True)
    created_at = models.DateTimeField('Create at', auto_now_add=True)

    class Meta:
        abstract = True
