from django.db import models
from django.utils import timezone
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# Create your models here.
class Users(models.Model):
	name = models.CharField(max_length = 200)
	surname = models.CharField(max_length = 200)
	user_type = models.IntegerField(default = 0)
	password = models.CharField(max_length = 200)
	email = models.CharField(max_length = 200)
	date_of_birth = models.DateTimeField('date of birth')

	def __str__(self):
		return self.name + " " +self.surname


class Requests(models.Model):
	activity_type = models.CharField(max_length = 100)
	timestamp = models.DateTimeField(default = timezone.now())
	users = models.ForeignKey(Users)
	requestStatus = models.CharField(max_length = 100)
	description = models.TextField()

	def __str__(self):
		return self.requestStatus

class Articles(models.Model):
	users = models.ForeignKey(Users)
	title = models.CharField(max_length = 200)
	articleStatus = models.CharField(max_length = 100)
	date_published = models.DateTimeField('date published')
	article_image = models.ImageField(upload_to = os.path.join(BASE_DIR, 'static', 'media'),)
	category = models.CharField(max_length = 200)

	def __str__(self):
		return self.title

class Content(models.Model):
	articles = models.ForeignKey(Articles)
	heading = models.CharField(max_length = 200)
	paragraph = models.TextField()

	def __str__(self):
		return str(self.articles) + ": " + str(self.heading)