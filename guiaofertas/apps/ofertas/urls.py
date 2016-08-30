from django.conf.urls import url

from guiaofertas.apps.ofertas.views import index, oferta, add, edit

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^novo/$', add, name='nova'),
    url(r'^editar/(?P<slug>[\w_-]+)/$', edit, name='editar'),
    #url(r'^tag/(?P<tag>[\w_-]+)/$', index, name='index_tagged'),
    url(r'^(?P<slug>[\w_-]+)/$', oferta, name='oferta'),
]
