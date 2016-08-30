from django.conf.urls import include, url

from guiaofertas.apps.empresas.views import empresa, index

urlpatterns = [
    url(r'^$', index, name='index'),
    #url(r'^tag/(?P<tag>[\w_-]+)/$', index, name='index_tagged'),
    url(r'^(?P<slug>[\w_-]+)/$', empresa, name='empresa'),
]
