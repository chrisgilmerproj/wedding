from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic import DetailView,TemplateView

from apps.weddings.models import Wedding

class WeddingView(TemplateView):
	
	template_name = 'homepage.html'

	def get_context_data(self,**kwargs):
		context = super(WeddingView, self).get_context_data(**kwargs)
		try:
			context['wedding'] = Wedding.objects.get(featured=True)
		except:
			context['wedding'] = None
		return context

