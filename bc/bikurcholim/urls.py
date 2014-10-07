from django.conf.urls import patterns, url

from bikurcholim import views
from bikurcholim.views import VolunteersDetailView
from bikurcholim.views import ClientsDetailView, CasesDetailView

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	url(r'^volunteers/$', views.volunteers, name='volunteers'),
	url(r'^clients/$', views.clients, name='clients'),
	url(r'^cases/$', views.cases, name='cases'),
	url(r'^clients/(?P<pk>\d+)/$', ClientsDetailView.as_view(), name='client-detail'),
	url(r'^volunteers/(?P<pk>\d+)/$', VolunteersDetailView.as_view(), name='volunteers-detail'),
	url(r'^cases/(?P<pk>\d+)/$', CasesDetailView.as_view(), name='cases-detail'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^export_xls/$', views.export_xls, name='export_xls'),
)