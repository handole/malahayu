from django.db import models
from redactor.fields import RedactorField

# Create your models here.

class Wisata(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=130, unique=True)
	image = models.ImageField(upload_to='wisata/%Y/%m', blank=True)
	content = RedactorField(verbose_name=u'Text')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('-created', '-updated')

	def __str__(self):
		return self.name


class PaketWisata(models.Model):
	name = models.CharField(max_length=100)
	content = RedactorField(verbose_name=u'Text')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name



