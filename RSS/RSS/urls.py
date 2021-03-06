from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'web.views.home', name='home'),
    url(r'^addnewcanal$', 'web.views.addnewcanal'),
    url(r'^three_more_feeds/$', 'web.views.three_more_feeds', name='three_more_feeds'),
)
