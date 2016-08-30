from guiaofertas.apps.ofertas.views.OfertaEditView import *
from guiaofertas.apps.ofertas.views.OfertaView import *
from guiaofertas.apps.ofertas.views.OfertasListView import *
from guiaofertas.apps.ofertas.views.OfertaAddView import *

oferta = OfertaView.as_view()
index = OfertasListView.as_view()
add = OfertaAddView.as_view()
edit = OfertaEditView.as_view()
