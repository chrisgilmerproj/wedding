from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic import DetailView,TemplateView

from apps.weddings.models import Wedding, Event, EventType

class WeddingView(TemplateView):
    
    template_name = 'homepage.html'

    def get_context_data(self,**kwargs):
        context = super(WeddingView, self).get_context_data(**kwargs)
        try:
            wedding = Wedding.objects.get(featured=True)
            ceremony = Event.objects.get(wedding=wedding,  type__slug='ceremony')
            rehearsal = Event.objects.get(wedding=wedding, type__slug='rehearsal')
            context['wedding'] = wedding
            context['ceremony'] = ceremony
            context['rehearsal'] = rehearsal
        except:
            context['wedding'] = None
            context['ceremony'] = None
            context['rehearsal'] = None
        return context

