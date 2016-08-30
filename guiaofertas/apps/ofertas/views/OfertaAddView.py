from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView

from guiaofertas.apps.ofertas.forms import OfertaModelFormExterno
from guiaofertas.apps.ofertas.models.Oferta import Oferta


class OfertaAddView(CreateView):
    model = Oferta
    template_name = 'ofertas/editaroferta.html'
    form_class = OfertaModelFormExterno

    # fields = (
    #     'empresa', 'categoria', 'produto', 'slug', 'descricao', 'preco_anterior', 'desconto', 'novo_preco', 'inicio_oferta',
    #     'fim_oferta', 'foto', 'tags')

    def post(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated():
            messages.error(self.request, 'Para cadastrar uma oferta é necessário estar logado' )
            return redirect(self.request.path)

        form = self.get_form()
        if form.is_valid():
            oferta = form.save(commit=False)
            if not self.request.user.is_superuser:
                oferta.empresa = self.request.user.empresa
            oferta.save()
            form.save_m2m()

        return render(request,'ofertas/index.html')