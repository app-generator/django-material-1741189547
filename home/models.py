# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    title = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Person(models.Model):

    #__Person_FIELDS__
    firstname = models.TextField(max_length=255, null=True, blank=True)
    lastname = models.TextField(max_length=255, null=True, blank=True)
    sex = models.IntegerField(null=True, blank=True)

    #__Person_FIELDS__END

    class Meta:
        verbose_name        = _("Person")
        verbose_name_plural = _("Person")


class Account(models.Model):

    #__Account_FIELDS__
    name_1 = models.TextField(max_length=255, null=True, blank=True)
    password_2 = models.TextField(max_length=255, null=True, blank=True)

    #__Account_FIELDS__END

    class Meta:
        verbose_name        = _("Account")
        verbose_name_plural = _("Account")


class Dept(models.Model):

    #__Dept_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    full_name = models.TextField(max_length=255, null=True, blank=True)

    #__Dept_FIELDS__END

    class Meta:
        verbose_name        = _("Dept")
        verbose_name_plural = _("Dept")



#__MODELS__END
