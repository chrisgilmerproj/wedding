
import datetime

from django.forms.models import inlineformset_factory
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from apps.guests.models import Group,Guest

def rsvp(request):
	query = request.GET.get('q','')

	if query:
		groups = Group.objects.filter(name__icontains=query)
	else:
		groups = []
	
	template_name = 'rsvp/rsvp.html'
	context = {
		'groups':groups,
		'query':query,
	}
	return render_to_response(
		template_name,
		context,
		context_instance=RequestContext(request)
		)

def rsvp_detail(request,**kwargs):
	group_id = kwargs.get('pk',None)
	group = get_object_or_404(Group,pk=group_id)

	GuestInlineFormset = inlineformset_factory(Group,Guest)
	if request.method == "POST":
		formset = BookInlineFormSet(request.POST, request.FILES, instance=author)
		if formset.is_valid():
			formset.save()
	else:
		formset = BookInlineFormSet(instance=author)
	
	template_name = 'rsvp/rsvp_detail.html'
	context = {
		'formset':formset,
		'group':group,
	}
	return render_to_response(
		template_name,
		context,
		context_instance=RequestContext(request)
		)

