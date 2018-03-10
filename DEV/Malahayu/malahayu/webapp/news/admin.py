from django.contrib import admin
from .models import News, Agenda, VisiMisi

# Register your models here.
class NewsAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug', 'image', 'content']
	prepopulated_fields = {'slug':('title',)}
admin.site.register(News, NewsAdmin)

class AgendaAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'content']
	prepopulated_fields = {'slug':('name',)}
admin.site.register(Agenda, AgendaAdmin)


class VisiAdmin(admin.ModelAdmin):
	list_display = ['title', 'content']
admin.site.register(VisiMisi, VisiAdmin)