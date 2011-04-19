from django.conf.urls.defaults import *

urlpatterns = patterns('apps.messages.views',
	url(r'^$', 'messages', name='messages'),
)
