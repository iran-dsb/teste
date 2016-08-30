from django.views.generic.detail import DetailView

from guiaofertas.apps.ofertas.models.Oferta import Oferta


class OfertaView(DetailView):
    model = Oferta
    template_name = 'ofertas/oferta.html'
