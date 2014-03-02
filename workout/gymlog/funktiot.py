# -*- coding: utf-8 -*-
# All classes and functions used by views


from models import workout, exercise
import datetime


class db:

	def fetch_db(self):

		date = workout.objects.latest('date')
		
		return(date)

	def tallenna_date(self):
		#Kun tallenetaan uusi treeni, tämä funktio
		#tallentaa timestampin 
		date = datetime.date.today()
		workout.objects.create(date=date)
		return

	def hae_liikkeet(self):

		liikkeet = exercise.objects.all()

		return (liikkeet)