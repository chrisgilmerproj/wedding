from django.conf import settings
from django.conf.urls.defaults import *
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

from weddings.views import WeddingView, EventDetailView

admin.autodiscover()
urlpatterns = patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    
	# Static Pages
    url(r'^$',            WeddingView.as_view(template_name='homepage.html'),   name="home"),
    url(r'^contact/$',    WeddingView.as_view(template_name='contact.html'),    name="contact"),
    url(r'^directions/$', WeddingView.as_view(template_name='directions.html'), name="directions"),
    url(r'^gallery/$',    WeddingView.as_view(template_name='gallery.html'),    name="gallery"),
    url(r'^program/$',    WeddingView.as_view(template_name='program.html'),    name="program"),
    url(r'^story/$',      WeddingView.as_view(template_name='story.html'),      name="story"),
	
	# Dynamic Pages
	url(r'^event/(?P<slug>\w+)/$', EventDetailView.as_view(), name="event_detail"),    
	url(r'^messages/', include('messages.urls')),
	url(r'^rsvp/',     include('rsvp.urls')),
)

# Static URLs
urlpatterns += staticfiles_urlpatterns()

# Upload URLS
if settings.DEBUG:
    urlpatterns.insert(-2, url(r'^%s(?P<path>.*)' % settings.MEDIA_URL[1:],
        'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))
