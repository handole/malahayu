from django.conf.urls import url
from django.views.generic import TemplateView
from .views import ImageList, VideoList

urlpatterns = [
	url(r'^foto/$', ImageList.as_view()),
	url(r'^video/$', VideoList.as_view()),
]