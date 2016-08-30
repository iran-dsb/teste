from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic.edit import UpdateView

from guiaofertas.apps.ofertas.forms import OfertaModelFormExterno
from guiaofertas.apps.ofertas.models.Oferta import Oferta


class OfertaEditView(UpdateView):
    model = Oferta
    template_name = 'ofertas/editaroferta.html'
    form_class = OfertaModelFormExterno

    # def form_invalid(self, form):
    #     import pdb;
    #     pdb.set_trace()

    def post(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated():
            messages.error(self.request, 'Para editar uma oferta é necessário estar logado')
            return redirect(self.request.path)

        self.object = self.get_object()
        #form = selfget_form()
        form = self.form_class(request.POST, request.FILES, instance=self.object)
        if form.is_valid():
            oferta = form.save(commit=False)
            if not self.request.user.is_superuser:
                oferta.empresa = self.request.user.empresa
            oferta.save()
            form.save_m2m()

        return redirect('oferta:index')
