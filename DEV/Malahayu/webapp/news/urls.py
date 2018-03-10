from django.conf.urls import url
from .views import NewsList, detailnews, AgendaList

urlpatterns = [
	url(r'^$', NewsList.as_view()),
	url(r'^(?P<slug>[-\w]+)/$', detailnews, name='news-detail'),
	
]