from django.db import models

from guiaofertas.apps.core.models.ModelBase import ModelBase
from guiaofertas.apps.empresas.models import Empresa


class Contato(ModelBase):
    nome = models.CharField('Nome', max_length=50, null=False, blank=False)
    telefone = models.CharField('Telefone', max_length=16, null=False, blank=False)
    ramal = models.IntegerField('Ramal', null=True, blank=True)
    celular = models.CharField('Celular', max_length=16, null=True, blank=True)
    email = models.EmailField('E-mail', max_length=100, null=True, blank=True)
    privado = models.BooleanField('Oculto')

    empresa = models.ForeignKey(
        Empresa, verbose_name='Empresa', related_name='contatos', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'
        ordering = ['-created']