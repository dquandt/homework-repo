from django.db import models
from django.contrib.auth.models import User

class Album(models.Model):
	title = models.CharField(max_length=75)
	def __unicode__(self):
		return self.title

class Image(models.Model):
	title = models.CharField(max_length=75, blank=True, null=True)
	image = models.FileField(upload_to="images/")
	albums = models.ManyToManyField(Album, blank=True)
	width = models.IntegerField(blank=True, null=True)
	height = models.IntegerField(blank=True, null=True)
	user = models.ForeignKey(User, null=True, blank=True)
	def __unicode__(self):
		return self.image.name




