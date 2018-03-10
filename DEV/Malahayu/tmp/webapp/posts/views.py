from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

# Create your views here.
class Index(TemplateView):
	template_name = 'index.html'

	def get_index(self, request):
		return HttpResponse(self.template_name)


