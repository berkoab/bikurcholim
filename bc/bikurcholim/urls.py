from django.conf.urls import patterns, url

from bikurcholim import views
from bikurcholim.views import VolunteersDetailView

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	url(r'^volunteers/$', views.volunteers, name='volunteers'),
	url(r'^clients/$', views.clients, name='clients'),
	url(r'^volunteers/(?P<pk>\d+)/$', VolunteersDetailView.as_view(), name='article-detail'),
	url(r'^login/$', views.user_login, name='login'),
)