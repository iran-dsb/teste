import re

from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)
from django.core import validators
from django.db import models

from guiaofertas.apps.empresas.models.Empresa import Empresa


class CustomUser(AbstractBaseUser, PermissionsMixin):
    empresa = models.ForeignKey(Empresa, verbose_name='Empresa', related_name='usuarios', null=True, blank=True)
    username = models.CharField(
        'Nome de Usuário',
        max_length=150,
        unique=True,
        validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'),
                                              'O nome de usuário só pode conter letras, digitos ou os '
                                              'seguintes caracteres: @/./+/-/_', 'invalid')],
        error_messages={
            'unique': ("Já existe um usuário com esse nome."),
        },
    )
    name = models.CharField('Nome', max_length=100, blank=True)
    email = models.EmailField('E-mail', unique=True)
    is_active = models.BooleanField('Está ativo?', blank=True, default=True)
    is_staff = models.BooleanField('É da equipe?', blank=True, default=False)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.name or self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'


