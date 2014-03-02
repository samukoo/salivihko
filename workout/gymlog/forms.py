# -*- coding: utf-8 -*-

from django import forms
from gymlog.models import workout, exercise

class ToistoForm(forms.ModelForm):
    
    toistot = forms.IntegerField(help_text="Toistojen lukumäärä")
    date = forms.CharField(widget=forms.DateInput(), max_length=128, help_text="Pvm")

    class Meta:
        # Provide an association between the ModelForm and a model
        model = workout
        #fields = ('date', 'toistot')

class LiikeForm(forms.ModelForm):

    liike = forms.CharField(widget=forms.TextInput(), max_length=40, help_text="Liike")

    class Meta:
      model =  exercise
        

#widget=forms.HiddenInput()








#class PageForm(forms.ModelForm):
 #   title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
  #  url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
   # views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    #class Meta:
        # Provide an association between the ModelForm and a model
     #   model = Page

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
      #  fields = ('title', 'url', 'views')