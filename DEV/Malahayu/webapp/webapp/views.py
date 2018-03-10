from django.shortcuts import render

from wisata.models import Wisata
from news.models import News, Agenda
from gallery.models import Video

# Create your views here.
def index(request):
	news = News.objects.order_by('-created')[:2]
	wisata = Wisata.objects.order_by('-created')[:2]
	agenda = Agenda.objects.filter(available=True)[:1]
	video = Video.objects.order_by('-created')[:1]

	context = {
		'news':news,
		'wisata':wisata,
		'agenda':agenda,
		'video':video,
	}
	return render(request, 'index.html', context)