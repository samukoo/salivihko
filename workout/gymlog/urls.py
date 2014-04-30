from django.conf.urls import patterns, url
from gymlog import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),
		url(r'save/$', views.save, name='save'),
		url(r'add_exercise/$', views.add_exercise, name='add_exercise'),
		url(r'new_workout/$', views.new_workout_page, name='new_workout_page'),
		url(r'uusi_treeni/$', views.uusi_treeni, name='uusi_treeni'),
		url(r'uusi_liike/$', views.uusi_liike, name='uusi_liike'),
		url(r'uusi_treeni/(?P<workout>[-\w]+)/$', views.history, name='history'),
		#url(r'search/$', views.search, name='search'),)
		)