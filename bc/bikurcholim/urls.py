from django.conf.urls import patterns, url

from bikurcholim import views
from bikurcholim.views import VolunteersDetailView, HousingScheduleDetailView
from bikurcholim.views import ClientsDetailView, CasesDetailView

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	url(r'^volunteers/$', views.volunteers, name='volunteers'),
	url(r'^clients/$', views.clients, name='clients'),
	url(r'^cases/$', views.cases, name='cases'),
	url(r'^housingschedule/$', views.housingschedule, name='housingschedule'),
	url(r'^clients/(?P<pk>\d+)/$', ClientsDetailView.as_view(), name='client-detail'),
	url(r'^volunteers/(?P<pk>\d+)/$', VolunteersDetailView.as_view(), name='volunteers-detail'),
	url(r'^cases/(?P<pk>\d+)/$', CasesDetailView.as_view(), name='cases-detail'),
	url(r'^housingschedule/(?P<pk>\d+)/$', HousingScheduleDetailView.as_view(), name='housingschedule-detail'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^export_xls/$', views.export_xls, name='export_xls'),
	url(r'^cases_advanced/$', views.cases_advanced, name='cases_advanced'),
	url(r'^volunteers_advanced/$', views.volunteers_advanced, name='volunteers_advanced'),
	url(r'^clients_advanced/$', views.clients_advanced, name='clients_advanced'),
	url(r'^housingschedule_advanced/$', views.housingschedule_advanced, name='housingschedule_advanced'),
	url(r'^events/$', views.events, name='events'),
	url(r'^test/$', views.test, name='test'),
)