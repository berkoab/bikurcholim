from django.conf.urls import patterns, include, url
from django.contrib import admin
from model_report import report
report.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bc.views.home', name='home'),
    url(r'^$', include('bikurcholim.urls')),
    url(r'^bikurcholim/', include('bikurcholim.urls')),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
)
