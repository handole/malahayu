from django.db import models
from redactor.fields import RedactorField

# Create your models here.
class News(models.Model):
	title = models.CharField(max_length=150)
	slug = models.SlugField(max_length=180, unique=True)
	image = models.ImageField(upload_to='news/%Y/%m', blank=True)
	content = RedactorField(verbose_name=u'Text')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('-created', '-updated')

	def __str__(self):
		return self.title


class Agenda(models.Model):
	name = models.CharField(max_length=150)
	slug = models.SlugField(max_length=200, unique=True)
	content = RedactorField(verbose_name=u'Text')
	available = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('-created', '-updated')

	def __str__(self):
		return self.name


class VisiMisi(models.Model):
	title = models.CharField(max_length=100)
	content = RedactorField(verbose_name=u'Text')

	def __str__(self):
		return self.title
