from django.conf.urls import patterns, url
from gymlog import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),
		url(r'save/$', views.save, name='save'),
		url(r'add_exercise/$', views.add_exercise, name='add_exercise'),
		url(r'new_workout/$', views.new_workout_page, name='new_workout_page'),

		#url(r'ajoneuvo/(?P<reknum>[-\w]+)/$', views.ajoneuvo, name='ajoneuvo'),
		#url(r'search/$', views.search, name='search'),)
		)