from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Image, Video

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
	list_display = ['name', 'image']
admin.site.register(Image, ImageAdmin)

class VideoAdmin(AdminVideoMixin, admin.ModelAdmin):
	list_display = ['name', 'link']
admin.site.register(Video, VideoAdmin)
