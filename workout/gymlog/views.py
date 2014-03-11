# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from gymlog.forms import ToistoForm, LiikeForm
from django.shortcuts import redirect
from models import *

from gymlog import funktiot

#import *

def index(request):
	context = RequestContext(request)
	
	a = funktiot.db()
	
	#fetch_db() hakee viimeisimmän treenin päivämäärän
	last_workout = a.fetch_db()
	
	testi = workout.objects.all()
	liikkeet = a.hae_liikkeet()



	#Syötetään context_dict muuttujalle data
	context_dict = {'last_workout' : last_workout,
	'liikkeet' : liikkeet,
	'sarjat' : testi
	}
	
	#Lähetetään keräilty data html rederöitäväksi
	return render_to_response('gymlog/index.html',context_dict, context)

def save(request):
	#TÄmä paska pitäisi refaktoroida.
	#modaillaan silleen että palauttaa onnistuneessa responsessa kannasta jotain kamaa
	context = RequestContext(request)
	# POST?
	if request.method == 'POST':
		#Jos metodi == POST tallennetaan POST body kontentti muuttujaan
		form = ToistoForm(request.POST)

		if form.is_valid():
			form.save(commit=True)
			return HttpResponse("Save ok!")
		else:
			#return index(request)
			return HttpResponse(form.errors)
		#Jos ei posti, tyhjä formi
	else:
		form = ToistoForm()
	return render_to_response('gymlog/add.html', {'form': form}, context)

def add_exercise(request):

	context=RequestContext(request)
	form = LiikeForm(request.POST)
	if form.is_valid():
		form.save(commit=True)
		return redirect('index')
	else:
		return HttpResponse("vituixman")

def new_workout_page(request):

	context=RequestContext(request)


	return render_to_response('gymlog/new_workout.html', context)







def apu_request(request):
	context=RequestContext(request)

	_data_count = workout.objects.count()
	_data_set = workout.objects.all()


	return HttpResponse(_data_set)






