from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from .models import Wisata, PaketWisata

# Create your views here.

class WisataList(ListView):
	queryset = Wisata.objects.all()
	context_object_name = 'list_wisata'
	template_name = 'list_wisata.html'


def detailwisata(request, slug):
	instance = get_object_or_404(Wisata, slug=slug)
	return render(request, 'detail_wisata.html', {'instance':instance})

class PaketWisata(ListView):
	queryset = PaketWisata.objects.all()
	context_object_name = 'paket_wisata'
	template_name = 'paket_wisata.html'