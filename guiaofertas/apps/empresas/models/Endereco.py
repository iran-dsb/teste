from django.db import models

from guiaofertas.apps.core.models.ModelBase import ModelBase
from guiaofertas.apps.core.models.abstratas.Uf import Uf
from guiaofertas.apps.empresas.models import Empresa


class Endereco(ModelBase):
    logradouro = models.CharField("Logradouro", null=False, blank=False, max_length=150)
    numero = models.CharField("Número", null=False, blank=False, max_length=30)
    bairro = models.CharField("Bairro", null=False, blank=False, max_length=150)
    cidade = models.CharField("Cidade", null=False, blank=False, max_length=150)
    cep = models.CharField("CEP", null=False, blank=False, max_length=9)
    uf = models.CharField(max_length=2,
                          choices=((x.name, x.value) for x in Uf),
                          default=Uf.RJ,
                          null=False, blank=False)
    complemento = models.CharField("Complemento", null=False, blank=True, max_length=150)

    latitude = models.DecimalField("Latitude", max_digits=15, decimal_places=12, null=True, blank=True)
    longitude = models.DecimalField("Latitude", max_digits=15, decimal_places=12, null=True, blank=True)

    empresa = models.ForeignKey(
        Empresa, verbose_name='Empresa', related_name='enderecos', on_delete=models.CASCADE
    )

    privado = models.BooleanField('Oculto')

    def __str__(self):
        return '{self.logradouro} {self.numero}, {self.bairro} - {self.cidade} - {self.uf}'.format(self=self)


    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
        ordering = ['-created']