from django.db import models

# Create your models here.
class myUsers(models.Model):
	name = models.CharField(max_length = 200)
	email = models.CharField(max_length = 200)
	password = models.IntegerField()

	def __str__(self):
		return self.name		