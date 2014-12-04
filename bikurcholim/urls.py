from django.conf.urls import patterns, url

from bikurcholim import views
from bikurcholim.views import VolunteersDetailView, HousingScheduleDetailView
from bikurcholim.views import IntakeCallsDetailView, CasesDetailView
from bikurcholim.views import TasksDetailView, ClientServiceDetailView

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	url(r'^volunteers/$', views.volunteers, name='volunteers'),
	url(r'^cases/$', views.cases, name='cases'),
	url(r'^intakecalls/$', views.intakecalls, name='intakecalls'),
	url(r'^tasks/$', views.tasks, name='tasks'),
	url(r'^clientservice/$', views.clientservice, name='clientservice'),
	url(r'^housingschedule/$', views.housingschedule, name='housingschedule'),
	url(r'^cases/(?P<pk>\d+)/$', CasesDetailView.as_view(), name='cases-detail'),
	url(r'^volunteers/(?P<pk>\d+)/$', VolunteersDetailView.as_view(), name='volunteers-detail'),
	url(r'^intakecalls/(?P<pk>\d+)/$', IntakeCallsDetailView.as_view(), name='intakecalls-detail'),
	url(r'^tasks/(?P<pk>\d+)/$', TasksDetailView.as_view(), name='tasks-detail'),
	url(r'^clientservice/(?P<pk>\d+)/$', ClientServiceDetailView.as_view(), name='clientservice-detail'),
	url(r'^housingschedule/(?P<pk>\d+)/$', HousingScheduleDetailView.as_view(), name='housingschedule-detail'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^export_xls/$', views.export_xls, name='export_xls'),
	url(r'^intakecalls_advanced/$', views.intakecalls_advanced, name='intakecalls_advanced'),
	url(r'^tasks_advanced/$', views.tasks_advanced, name='tasks_advanced'),
	url(r'^clientservice_advanced/$', views.clientservice_advanced, name='clientservice_advanced'),
	url(r'^volunteers_advanced/$', views.volunteers_advanced, name='volunteers_advanced'),
	url(r'^cases_advanced/$', views.cases_advanced, name='cases_advanced'),
	url(r'^housingschedule_advanced/$', views.housingschedule_advanced, name='housingschedule_advanced'),
	url(r'^events/$', views.events, name='events'),
	url(r'^casecalendar/$', views.casecalendar, name='casecalendar'),
	url(r'^housingcalendar/$', views.housingcalendar, name='housingcalendar'),
	url(r'^gotoevent/$', views.gotoevent, name='gotoevent'),
	url(r'^test/$', views.test, name='test'),
)