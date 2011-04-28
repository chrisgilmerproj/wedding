from django.conf import settings
from django.conf.urls.defaults import *
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

from weddings.views import WeddingView

admin.autodiscover()
urlpatterns = patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    
    url(r'^$',          WeddingView.as_view(template_name='homepage.html'), name="home"),
    url(r'^events/$',   WeddingView.as_view(template_name='events.html'),   name="events"),
    url(r'^lodging/$',  WeddingView.as_view(template_name='lodging.html'),  name="lodging"),
    url(r'^story/$',    WeddingView.as_view(template_name='story.html'),    name="story"),
    url(r'^gallery/$',  WeddingView.as_view(template_name='gallery.html'),  name="gallery"),
	url(r'^messages/',  include('messages.urls')),
    url(r'^registry/$', WeddingView.as_view(template_name='registry.html'), name="registry"),
    url(r'^contact/$',  WeddingView.as_view(template_name='contact.html'),  name="contact"),
	url(r'^rsvp/',      include('rsvp.urls')),
)

# Static URLs
urlpatterns += staticfiles_urlpatterns()

# Upload URLS
if settings.DEBUG:
    urlpatterns.insert(-2, url(r'^%s(?P<path>.*)' % settings.MEDIA_URL[1:],
        'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))
