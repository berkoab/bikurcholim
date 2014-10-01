from django.conf.urls import patterns, url

from bikurcholim import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	url(r'^volunteers/$', views.volunteers, name='volunteers'),
	url(r'^clients/$', views.clients, name='clients'),
)