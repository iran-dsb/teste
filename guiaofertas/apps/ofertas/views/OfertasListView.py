from django.views.generic.list import ListView

from guiaofertas.apps.ofertas.models.Oferta import Oferta


class OfertasListView(ListView):
    model = Oferta
    template_name = 'ofertas/index.html'
