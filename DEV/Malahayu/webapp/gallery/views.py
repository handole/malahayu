from django.shortcuts import render
from django.views.generic import ListView
from .models import Image, Video


# Create your views here.
class ImageList(ListView):
	model = Image
	template_name = 'image.html'
	paginate_by = 9
	queryset = Image.objects.all()

class VideoList(ListView):
	model = Video
	template_name = 'video.html'
	paginate_by = 5
	queryset = Video.objects.all()