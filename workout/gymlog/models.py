from django.db import models
from django.contrib.auth.models import User


class workout(models.Model):
	
	date = models.CharField(max_length=20)
	liike = models.CharField(max_length=30)
	toistot = models.IntegerField(default=0)
	kilot = models.IntegerField(default=0)
	user = models.CharField(max_length=20)

	def __unicode__(self):
		return self.date

class exercise(models.Model):

	liike = models.CharField(max_length=40)

	def __unicode__(self):
		return self.liike

class UserProfile(models.Model):

	user = models.OneToOneField(User)

	def __unicode__(self):
		return self.user.username









#nama ei tarpeellisia
#
#class treeni(models.Model):
#	pvm = models.CharField(max_length=20)
#	
#	def __unicode__(self):
#		return self.pvm
#
#	class Meta:
#		ordering = ('pvm',)

#class setti(models.Model):
#	liike = models.CharField(max_length=20)
#	treeni = models.ManyToManyField(treeni)
#
#	def __unicode__(self):
#		return self.liike
#
#	class Meta:
#		ordering = ('liike',)