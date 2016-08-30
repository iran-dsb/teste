from django.db import models

from guiaofertas.apps.core.models.ModelBase import ModelBase


class Empresa(ModelBase):
    nome_fantasia = models.CharField('Nome Fantasia', max_length=100, blank=False, null=False)
    razao_social = models.CharField('Razão Social', max_length=100, blank=False, null=False)

    cnpj = models.CharField('CNPJ', max_length=14, blank=True, null=False)

    slug = models.SlugField('Identificador', max_length=100, unique=True)

    descricao = models.CharField('Descrição', max_length=250, blank=True, null=False)

    logo = models.ImageField('Logomarca', upload_to='logos', null=True, blank=True)

    def __str__(self):
        return self.nome_fantasia

    @models.permalink
    def get_absolute_url(self):
        return ('empresa:empresa', (), {'slug': self.slug})
        #return reverse('empresa:empresa', kwargs={'slug': self.slug})Para usar dessa forma preciso retirar o decorator

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['-created']