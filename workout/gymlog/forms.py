# -*- coding: utf-8 -*-

from django import forms
from gymlog.models import workout, exercise, UserProfile
from django.contrib.auth.models import User

class ToistoForm(forms.ModelForm):
    
    toistot = forms.IntegerField(help_text="Toistojen lukumäärä")
    kilot = forms.IntegerField(help_text="kilot")
    date = forms.CharField(widget=forms.DateInput(), max_length=128, help_text="Pvm")
    liike = forms.CharField(help_text="liike")
    user = forms.CharField(help_text="user")

    class Meta:
        # Provide an association between the ModelForm and a model
        model = workout
       

class LiikeForm(forms.ModelForm):

    liike = forms.CharField(widget=forms.TextInput(), max_length=40, help_text="Liike")
    user = forms.CharField(help_text="user")
    class Meta:
      model =  exercise

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
          model = User
          fields = ('username','email','password','first_name', 'last_name')