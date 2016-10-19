# coding:utf-8
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(u'Nome de usuario', max_length=30, unique=True)
    email = models.EmailField(u'E-mail', unique=True)
    name = models.CharField('Nome', max_length=100, blank=True)
    is_active = models.BooleanField(u"Esta ativo?", blank=True, default=True)
    is_staff = models.BooleanField(u"É da equipe?", blank=True, default=False)
    date_joined = models.DateTimeField(
        'Data de entrada',
        auto_now_add=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        self.name or self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name  = u"Usúario"
        verbose_name_plural = u"Usúarios"


