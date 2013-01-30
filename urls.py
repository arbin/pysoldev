from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from pysoldev import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'pysoldev.views.home', name='home'),
    url(r'^$', 'pysoldev.app.views.index', name='index'),

)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',  
        {'document_root': settings.MEDIA_ROOT}),
    )
