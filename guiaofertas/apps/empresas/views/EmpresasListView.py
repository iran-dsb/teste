from django.views.generic import ListView

from guiaofertas.apps.empresas.models.Empresa import Empresa


class EmpresasListView(ListView):
    model = Empresa
    template_name = 'empresas/index.html'