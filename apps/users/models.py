from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import BaseModel
from . import choices
from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    username = models.CharField(max_length=128, unique=True)
    phone_number = PhoneNumberField(region='UZ', unique=True)
    email = models.EmailField(_('Email address'), unique=True)

    first_name = models.CharField(verbose_name=_('First name'), max_length=124)
    last_name = models.CharField(verbose_name=_('Last name'), max_length=124)
    profile_photo = models.ImageField(upload_to='images/accounts/profile/%Y/%m/%d/', blank=True, null=True)
    gender = models.CharField(choices=choices.GENDER, max_length=1, default='m')

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    groups = models.ManyToManyField('auth.Group', related_name='users', blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.email
