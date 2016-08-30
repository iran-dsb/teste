from django.conf.urls import url

from guiaofertas.apps.core import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
]
