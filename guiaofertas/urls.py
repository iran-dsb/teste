"""guiaofertas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from guiaofertas.apps.core import urls as core_url
from guiaofertas.apps.empresas import urls as empresa_url
from guiaofertas.apps.ofertas import urls as oferta_url
from guiaofertas.apps.accounts import urls as account_url
from django.conf import settings

urlpatterns = [
    url(r'^', include(core_url, namespace='core')),
    url(r'^accounts/', include(account_url, namespace='accounts')),
    url(r'^empresas/', include(empresa_url, namespace='empresa')),
    url(r'^ofertas/', include(oferta_url, namespace='oferta')),
    url(r'^admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)