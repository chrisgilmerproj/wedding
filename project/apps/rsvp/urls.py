from django.conf.urls.defaults import *

urlpatterns = patterns('apps.rsvp.views',
	url(r'^$', 'rsvp', name='rsvp'),
	url(r'^(?P<pk>[\d]+)/$', 'rsvp_detail', name='rsvp_detail'),
)
