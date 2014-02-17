from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^e/(?P<path>.*)$', 'django.views.static.serve',
    #    { 'document_root': settings.STATIC_DOC_ROOT }),
    url(r'^', include('endpoint.urls')),
)
