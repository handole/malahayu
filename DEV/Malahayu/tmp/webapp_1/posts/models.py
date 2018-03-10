from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=200)
	image = models.ImageField(upload_to='image/%Y/%m', blank=True)
	content = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('-updated', '-created')

	def __init__(self):
		return self.title

 
