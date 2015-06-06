from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'homeless.views.home', name='home'),

    url(r'^search/$', 'homeless.views.search', name='search'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^homeless/$', 'homeless.views.homeless', name='homeless'),

    url(r'^donators/$', 'homeless.views.donators', name='donators'),

    url(r'^admin/', include(admin.site.urls)),
)
