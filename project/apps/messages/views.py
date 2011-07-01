from django.shortcuts import render_to_response
from django.template import RequestContext

from apps.messages.forms import MessageForm
from apps.messages.models import Message
from apps.weddings.models import Wedding

def messages(request):
    """ View to leave a message and see everyone's messages """
    
    wedding = Wedding.objects.get(featured=True)
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
        'form': form,
        'messages': message_list,
        'wedding': wedding,
    }
    return render_to_response(
        template_name,
        context,
        context_instance=RequestContext(request)
        )

