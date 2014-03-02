from django.conf.urls import patterns, url
from gymlog import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),
		url(r'save/$', views.save, name='save'),
		url(r'add_exercise/$', views.add_exercise, name='add_exercise'),
		url(r'apu_request/$', views.apu_request, name='apu_request'),


		#url(r'ajoneuvo/(?P<reknum>[-\w]+)/$', views.ajoneuvo, name='ajoneuvo'),
		#url(r'search/$', views.search, name='search'),)
		)