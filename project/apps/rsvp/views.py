from django.forms.models import inlineformset_factory
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from apps.rsvp.forms import GroupForm
from apps.rsvp.models import Group,Guest

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

	GuestInlineFormSet = inlineformset_factory(Group,Guest,
			extra=group.number_guests, max_num=group.number_guests)
	if request.method == "POST":
		form    = GroupForm(request.POST, instance=group)
		formset = GuestInlineFormSet(request.POST, instance=group)
		if form.is_valid() and formset.is_valid():
			form.save()
			formset.save()
	else:
		form    = GroupForm(instance=group)
		formset = GuestInlineFormSet(instance=group)
	
	template_name = 'rsvp/rsvp_detail.html'
	context = {
		'form':form,
		'formset':formset,
		'group':group,
	}
	return render_to_response(
		template_name,
		context,
		context_instance=RequestContext(request)
		)

