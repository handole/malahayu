from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.
class Image(models.Model):
	name = models.CharField(max_length=100)
	image = models.ImageField(upload_to='gallery/%Y/%m', blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('-created', '-updated')

	def __str__(self):
		return self.name


class Video(models.Model):
	name = models.CharField(max_length=100)
	link = EmbedVideoField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('-created', '-updated')

	def __str__(self):
		return self.name