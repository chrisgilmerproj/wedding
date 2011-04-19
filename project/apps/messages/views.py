from django.shortcuts import render_to_response
from django.template import RequestContext

from apps.messages.forms import MessageForm
from apps.messages.models import Message

def messages(request):
	""" View to leave a message and see everyone's messages """
	
	message_list = Message.objects.all()

	if request.method == "POST":
		form = MessageForm(request.POST)
		if form.is_valid(): 
			form.save()
			form = MessageForm()
	else:
		form = MessageForm()
	
	template_name = 'messages/messages.html'
	context = {
		'form':form,
		'messages':message_list,
	}
	return render_to_response(
		template_name,
		context,
		context_instance=RequestContext(request)
		)

