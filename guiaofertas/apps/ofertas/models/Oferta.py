from django.db import models
from taggit.managers import TaggableManager

from guiaofertas.apps.core.models.ModelBase import ModelBase
from guiaofertas.apps.empresas.models.Empresa import Empresa
from guiaofertas.apps.ofertas.models.Categoria import Categoria


class Oferta(ModelBase):

    def upload_to(instance, filename):
        return 'ofertas/empresa_{0}/{1}'.format(instance.empresa.pk, filename)

    produto = models.CharField("Produto", max_length=100, null=False,blank=False)
    slug = models.SlugField('Identificador', max_length=300, unique=True)
    descricao = models.CharField("Descrição", max_length=250, null=True, blank=True)
    preco_anterior = models.DecimalField("Preço Anterior", max_digits=9, decimal_places=2, null=True, blank=True)
    desconto = models.DecimalField("Desconto (%)", max_digits=4, decimal_places=2, null=True, blank=True)
    novo_preco = models.DecimalField("Novo Preço", max_digits=9, decimal_places=2, null=False, blank=False)
    inicio_oferta = models.DateTimeField("Início da Oferta", null=False, blank=False)
    fim_oferta = models.DateTimeField("Término da Oferta", null=False, blank=False)
    empresa = models.ForeignKey(to=Empresa,
                                verbose_name='Empresa',
                                related_name='ofertas',
                                on_delete=models.CASCADE)

    foto = models.ImageField('Foto', upload_to=upload_to)

    tags = TaggableManager(blank=True)

    categoria = models.ForeignKey(to=Categoria,
                                verbose_name='Categoria',
                                related_name='ofertas',
                                on_delete=models.CASCADE)

    def __str__(self):
        return self.produto

    @models.permalink
    def get_absolute_url(self):
        return ('oferta:oferta', (), {'slug': self.slug})


