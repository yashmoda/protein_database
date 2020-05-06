"""Protein_Database URL Configuration

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
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from proteins.views import get_admet_properties, get_properties, add_classification, add_regression, add_lipopetide, \
    add_ligand, add_applications, add_references, add_properties

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admet/', get_properties),
    url(r'^add_classification/', add_classification),
    url(r'^add_regression/', add_regression),
    url(r'^add_references/', add_references),
    url(r'^add_lipopetide/', add_lipopetide),
    url(r'^add_properties/', add_properties),
    url(r'^add_applications/', add_applications),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
