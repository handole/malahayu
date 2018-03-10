from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from .models import News, Agenda, VisiMisi
# Create your views here.

class NewsList(ListView):
	model = News
	template_name = 'news.html'
	context_object_name = 'news'
	paginate_by = 1
	queryset = News.objects.all()



def detailnews(request, slug):
	instance = get_object_or_404(News, slug=slug)
	return render(request, 'news_detail.html', {'instance':instance})


class AgendaList(ListView):
	model = Agenda
	template_name = 'agenda.html'
	paginate_by = 5
	queryset = Agenda.objects.all()

class VisiList(ListView):
	model = VisiMisi
	template_name = 'visimisi.html'
	queryset = VisiMisi.objects.all()