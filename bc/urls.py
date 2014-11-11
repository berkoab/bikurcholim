from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('bikurcholim.urls')),
    url(r'^bikurcholim/', include('bikurcholim.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
