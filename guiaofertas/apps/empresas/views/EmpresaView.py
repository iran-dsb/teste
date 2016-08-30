from django.views.generic import DetailView

from guiaofertas.apps.empresas.models.Empresa import Empresa


class EmpresaView(DetailView):
    model = Empresa
    template_name = 'empresas/empresa.html'

    # def get_context_data(self, **kwargs):
    #     context = super(EmpresaView, self).get_context_data(**kwargs)
    #     context['tags'] = Empresa.tags.all()
    #     return context