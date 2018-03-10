from django import forms

from django.contrib import admin
from .models import Wisata, PaketWisata

# Register your models here.
class WisataAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'content']
	prepopulated_fields = {'slug': ('name',)}
admin.site.register(Wisata, WisataAdmin)


class PaketAdmin(admin.ModelAdmin):
	list_display = ['name', 'content']
admin.site.register(PaketWisata, PaketAdmin)
