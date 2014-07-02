from django.conf.urls import patterns, include, url

from django.contrib import admin

from pysoldev import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'pysoldev.views.home', name='home'),
    url(r'^$', 'pysoldev.app.views.index', name='index'),
    url(r'^arbin/', 'pysoldev.views.arbin', name='arbin'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    )
