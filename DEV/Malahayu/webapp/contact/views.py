from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
# from django.views.generic.edit import FormView, CreateView
from django.contrib import messages
from .forms import ContactForm


# Create your views here.
# class ContactView(FormView, CreateView):
# 	template_name = 'contact.html'
# 	form_class = ContactForm
# 	success_url = '/contact/success/'


def contactform(request):
	form = ContactForm(request.POST)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		print('success')
	else:
		print(form.errors)
	return render(request, 'contact.html', {'form':form})


