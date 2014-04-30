# -*- coding: utf-8 -*-


from django.http import *
from django.template import RequestContext
from django.shortcuts import render_to_response
from gymlog.forms import ToistoForm, LiikeForm
from django.shortcuts import redirect
from models import *

from gymlog import funktiot


def index(request):
	context = RequestContext(request)
	a = funktiot.db()
	pvm = a.hae_pvm()


	context_dict = {'pvm' : pvm}
	return render_to_response('gymlog/index.html',context_dict, context)

def history(request, workout):

	context = RequestContext(request)

	workout = workout.replace('_','.')

	context_dict = {'pvm' : workout}

	return render_to_response('gymlog/uusi_treeni.html', context_dict ,context)


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
			return HttpResponseBadRequest("Lisaa liike!")
		

def add_exercise(request):
	#Tämä tallentaa kantaan uuden liikkeen
	context=RequestContext(request)
	form = LiikeForm(request.POST)
	if form.is_valid():
		form.save(commit=True)
		return redirect('new_workout_page')
	else:
		return HttpResponse("vituixman")

def uusi_treeni(request):

	context=RequestContext(request)

	#Pyydetään päivämäärä
	a=funktiot.db()
	pvm = a.hae_pvm()

	context_dict = {'pvm':pvm}

	return render_to_response('gymlog/uusi_treeni.html', context_dict ,context)



def new_workout_page(request):

	context=RequestContext(request)

	a=funktiot.db()
	liikkeet=a.hae_liikkeet()
	pvm = a.hae_pvm()
	context_dict = {'liikkeet' : liikkeet,
					'pvm':pvm}

	return render_to_response('gymlog/new_workout.html', context_dict ,context)

def uusi_liike(request):
	context=RequestContext(request)

	return render_to_response('gymlog/uusi_liike.html' ,context)

