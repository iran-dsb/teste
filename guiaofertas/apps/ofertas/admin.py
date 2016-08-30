from django.contrib import admin

# Register your models here.

from guiaofertas.apps.ofertas.forms import OfertaModelForm
from guiaofertas.apps.ofertas.models.Categoria import Categoria
from guiaofertas.apps.ofertas.models.Oferta import Oferta


class CategoriaInlineAdmin(admin.TabularInline):
    model = Categoria
    extra = 0


class OfertaAdmin(admin.ModelAdmin):
    list_display = ['produto', 'preco_anterior', 'desconto', 'novo_preco', 'inicio_oferta', 'fim_oferta', 'created',
                    'modified']
    #fields = ('categoria', 'produto', 'slug', 'descricao', 'preco_anterior', 'desconto', 'novo_preco', 'inicio_oferta',
    #          'fim_oferta', 'empresa', 'foto', 'tags')
    search_fields = ['produto', 'empresa', 'inicio_oferta', 'fim_oferta']
    prepopulated_fields = {'slug': ('produto', 'empresa')}
    form = OfertaModelForm


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cat_pai']
    fields = ['nome', 'slug', 'cat_pai']
    search_fields = ['nome', ]
    prepopulated_fields = {'slug': ('cat_pai', 'nome')}

    inlines = [CategoriaInlineAdmin, ]


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Oferta, OfertaAdmin)
