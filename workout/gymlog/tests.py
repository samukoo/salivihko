# -*- coding: utf-8 -*-

from django.test import TestCase
from gymlog import views
from gymlog import funktiot
from gymlog.models import workout, exercise
import datetime

class ViewTest(TestCase):
    
    def create_data(self):
    	date = datetime.date.today()
    	numero = "1"
    	workout.objects.create(date=date,toistot=numero)
    	return

    def test_index(self):
    	a = self.create_data()
    	response = self.client.get('/gymlog/')
    	self.assertEqual(response.status_code, 200)

    def test_save_exercise(self):
    	response = self.client.post('/gymlog/save/', {'toistot':'1','date':'1'})
    	self.assertEqual(response.status_code, 200)

    def test_tallenna_uusi_liike(self):
    	response = self.client.post('/gymlog/add_exercise/', {'liike':'Pena'})
    	self.assertEqual(response.status_code,302)

    def test_tallenna_uusi_liike_fail(self):
    	response = self.client.post('/gymlog/add_exercise/', {'liike':''})
    	self.assertNotEqual(response.status_code,302)
    

class FunktiotTest(TestCase):

	def test_hae_liikkeet(self):

		teksti = "penkkipunnerrus"
		exercise.objects.create(liike=teksti)
		
		a = funktiot.db()
		liikkeet = a.hae_liikkeet()
		self.assertNotEqual(liikkeet[0], "NULL")







	def test_funk_tallenna_date(self):
			#funktio tallentaa päivän kantaan
			#mikäli tallennus ei onnistu, get feilaa ja testi feilaa
			a = funktiot.db()
			a.tallenna_date()
			workout.objects.get(pk=1)






class ModelTest(TestCase):
	
	def create_data_workout(self):
		#workout taulu
		date = datetime.date.today()
		numero = "1"
		workout.objects.create(date=date,toistot=numero)
		return

	def create_data_exercise(self):
		#populoidaan exercise taulua
		data = "penkkipunnerrus" 
		exercise.objects.create(liike=data)
		return

	def test_kanta_exercise_tallenna_ja_hae(self):

		a = self.create_data_exercise()
		data = exercise.objects.count()
		self.assertEqual(data, 1)


	def test_kanta_workout_tallenna_ja_hae(self):
		#Testataan onko kantaa olemassa
		#1: tallenna kantaan
		a = self.create_data_workout()
		#2: lue kannasta eka objecti. failaa jos tyhjä 
		data = workout.objects.get(pk=1)

	

