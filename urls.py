from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from pysoldev import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    # Examples:
    url(r'^$', 'pysoldev.views.home', name='home'),
    # url(r'^pysoldev/', include('pysoldev.foo.urls')),
    url(r'^$', 'pysoldev.app.views.index', name='index'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^arbin/', 'pysoldev.views.arbin', name='arbin'),
    url(r'^captcha/', include('captcha.urls')),

)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',  
        {'document_root': settings.MEDIA_ROOT}),
    )