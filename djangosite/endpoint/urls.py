from django.conf.urls import patterns, include, url

from .views import IndexView, DetailView, AuthView

urlpatterns = patterns('',
	url(r'^(?P<slug>[-\w]+)/$', DetailView.as_view(), name='endpoint'),
    url(r'^$', IndexView.as_view(), name='index'),
	url(r'^auth/(?P<slug>[-\w]+)/$', AuthView.as_view(), name='auth_endpoint'),
)
