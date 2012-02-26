from django.conf import settings
from django.conf.urls.defaults import include, patterns, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView


admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),

    url(r'^$', TemplateView.as_view(template_name='homepage.html'), name="home"),
    url(r'^events/$', TemplateView.as_view(template_name='events.html'), name="events"),
    url(r'^lodging/$', TemplateView.as_view(template_name='lodging.html'), name="lodging"),
    url(r'^gallery/$', TemplateView.as_view(template_name='gallery.html'), name="gallery"),
    url(r'^registry/$', TemplateView.as_view(template_name='registry.html'), name="registry"),
    url(r'^contact/$', 'messages.views.messages', name='contact'),
    url(r'^rsvp/', include('rsvp.urls')),
    url(r'^RSVP/', include('rsvp.urls')),
)

# Static URLs
urlpatterns += staticfiles_urlpatterns()

# Upload URLS
if settings.DEBUG:
    urlpatterns.insert(-2, url(r'^%s(?P<path>.*)' % settings.MEDIA_URL[1:],
        'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))
