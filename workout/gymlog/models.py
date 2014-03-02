from django.db import models

# Create your models here.
class workout(models.Model):
	
	date = models.CharField(max_length=20)
	toistot = models.IntegerField(default=0)

	def __unicode__(self):
		return self.date

class exercise(models.Model):

	liike = models.CharField(max_length=40)

	def __unicode__(self):
		return self.liike