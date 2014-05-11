# -*- coding: utf-8 -*-


from django.http import *
from django.template import RequestContext
from django.shortcuts import render_to_response
from gymlog.forms import ToistoForm, LiikeForm, UserForm
from django.shortcuts import redirect
from models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
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


@login_required
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

def register(request):

	context = RequestContext(request)

	registered = False

	#Jos request on POST
	if request.method == 'POST':

		user_form = UserForm(data=request.POST)

		if user_form.is_valid():

			user = user_form.save()
			user.set_password(user.password)
			user.save()

			registered = True
		else:
			print user_form.errors

	#Jos request on GET
	else:
		user_form = UserForm()

	return render_to_response(
		'gymlog/register.html',
		{'user_form':user_form, 'registered': registered},
		context)

def user_login(request):

	context = RequestContext(request)

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/gymlog/')
			else:
				return HttpResponse("account not activated/disabled.")

		else:
			return HttpResponse ("invalid login credentials")

	else:
		return render_to_response('gymlog/login.html', {}, context)

@login_required
def user_logout(request):

	logout(request)

	return HttpResponseRedirect('/gymlog/')

@login_required
def restricted(request):
	return HttpResponse("restricteed aaareaaa")

