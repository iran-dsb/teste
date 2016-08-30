from django import forms
from django.contrib.admin.widgets import AdminFileWidget
from django.core.exceptions import ValidationError
from django.forms import FileInput

from guiaofertas.apps.core.utils.widgets import NotClearableFileInput
from guiaofertas.apps.empresas.models.Empresa import Empresa
from guiaofertas.apps.ofertas.models.Oferta import Oferta


class OfertaModelForm(forms.ModelForm):
    #tags = TagField(required=False)
    class Meta:
        model = Oferta
        fields = (
        'categoria', 'produto', 'slug', 'descricao', 'preco_anterior', 'desconto', 'novo_preco', 'inicio_oferta',
        'fim_oferta', 'empresa', 'foto', 'tags')


class OfertaModelFormExterno(forms.ModelForm):
    empresa = forms.ModelChoiceField(queryset=Empresa.objects.all().order_by('nome_fantasia'), required=False)
    foto = forms.ImageField(required=False, widget=NotClearableFileInput)

    class Meta:
        model = Oferta
        fields = ('empresa', 'categoria', 'produto', 'slug', 'descricao', 'preco_anterior', 'desconto', 'novo_preco',
                  'inicio_oferta', 'fim_oferta', 'foto', 'tags')
        widgets = {
            'foto': forms.FileInput()
        }