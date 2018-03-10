from django.conf.urls import url
from .views import WisataList, detailwisata, PaketWisata


urlpatterns = [
	url(r'^$', WisataList.as_view()),
	url(r'^(?P<slug>[-\w]+)/$', detailwisata, name='wisata-detail'),
	# url(r'^paket-wisata-detail/$', TemplateView.as_view(template_name='detail_paketwisata.html')),
]