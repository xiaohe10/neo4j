from django.conf.urls import patterns, include, url
from django.contrib import admin
from web.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'neo4j.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',viewRecommendation),
    # url(r'^admin/', include(admin.site.urls)),
)
