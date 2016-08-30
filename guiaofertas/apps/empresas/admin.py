from django.contrib import admin

# Register your models here.
from guiaofertas.apps.empresas.models.Endereco import Endereco
from guiaofertas.apps.empresas.models.Contato import Contato
from guiaofertas.apps.empresas.models.Empresa import Empresa


class ContatoAdmin(admin.ModelAdmin):

    fields = ['nome', ('telefone', 'ramal'), 'celular', 'email', 'empresa', 'privado']
    list_display = ['nome', 'telefone', 'email', 'created', 'modified', 'privado']
    search_fields = ['nome', 'email']


class EnderecoAdmin(admin.ModelAdmin):

    list_display = ['logradouro', 'numero', 'bairro', 'cidade', 'uf', 'created', 'modified', 'privado']
    search_fields = ['uf', 'cidade', 'bairro']


class ContatoInlineAdmin(admin.TabularInline):
    model = Contato
    extra = 0


class EnderecoInlineAdmin(admin.StackedInline):
    model = Endereco
    extra = 0


class EmpresaAdmin(admin.ModelAdmin):

    list_display = ['nome_fantasia', 'razao_social', 'created', 'modified']
    fields = ['nome_fantasia', 'slug', 'razao_social', 'cnpj', 'descricao', 'logo']
    search_fields = ['nome_fantasia', 'razao_social', 'cnpj']
    prepopulated_fields = {'slug': ('nome_fantasia',)}

    inlines = [
        ContatoInlineAdmin,
        EnderecoInlineAdmin,
    ]

admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Contato, ContatoAdmin)
admin.site.register(Endereco, EnderecoAdmin)