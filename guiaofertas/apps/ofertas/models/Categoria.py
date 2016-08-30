from django.db import models

from guiaofertas.apps.core.models.ModelBase import ModelBase


class Categoria(ModelBase):
    nome = models.CharField('Categoria', max_length=60, null=False, blank=False)
    slug = models.SlugField('Identificador', max_length=300, unique=True)
    cat_pai = models.ForeignKey(to='self',
                                null=True,
                                blank=True,
                                verbose_name='Categoria Pai',
                                related_name='subcategorias',
                                on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
