from django.conf.urls import patterns, include, url

from .views import IndexView, DetailView

urlpatterns = patterns('',
	url(r'^(?P<slug>[-\w]+)/$', DetailView.as_view(), name='endpoint'),
    url(r'^$', IndexView.as_view(), name='index'),
)