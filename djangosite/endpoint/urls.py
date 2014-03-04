from django.conf.urls import patterns, include, url

from .views import IndexView, DetailView, AuthView, MockObjectView

urlpatterns = patterns('',
	url(r'^(?P<slug>[-\w]+)/$', DetailView.as_view(), name='endpoint'),
    url(r'^$', IndexView.as_view(), name='index'),
	url(r'^auth/(?P<slug>[-\w]+)/$', AuthView.as_view(), name='auth_endpoint'),
    url(r'^mock_objects/(?P<class_name>[_\w]+)/(?P<object_id>[-\w\d]+)/$', MockObjectView.as_view(), name='mock_objects'),
)
