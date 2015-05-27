from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=200)
	date = models.DateTimeField(default = timezone.now())

	def __str__(self):
		return self.title

class Content(models.Model):
	article = models.ForeignKey(Article)
	heading = models.TextField()
	paragraph = models.TextField()

	def __str__(self):
		return self.heading