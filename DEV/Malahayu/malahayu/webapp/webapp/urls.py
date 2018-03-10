"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from contact.views import contactform
from wisata.views import PaketWisata
from news.views import AgendaList, VisiList
from .views import index


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', index, name='index'),
    url(r'^wisata/', include('wisata.urls', namespace='wisata')),
    url(r'^news/', include('news.urls', namespace='news')),
    url(r'^gallery/', include('gallery.urls', namespace='gallery')),

    url(r'^redactor/', include('redactor.urls')),
   
    url(r'^profil/', TemplateView.as_view(template_name='profil.html')),
    url(r'^visimisi/', VisiList.as_view()),
    url(r'^agenda/', AgendaList.as_view()),
    url(r'^faqs/', TemplateView.as_view(template_name='faqs.html')),
    url(r'^paket-wisata/$', PaketWisata.as_view()),
    url(r'^contact/', contactform, name='contact'),
    url(r'^contact/success/', TemplateView.as_view(template_name='success.html'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)