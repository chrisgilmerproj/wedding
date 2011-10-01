from apps.weddings.models import Wedding, Event, EventType


def wedding(request):

    wedding = Wedding.objects.get(featured=True)
    ceremony = Event.objects.get(wedding=wedding,  type__slug='ceremony')
    rehearsal = Event.objects.get(wedding=wedding, type__slug='rehearsal')
    context = {
        'wedding': wedding,
        'ceremony': ceremony,
        'rehearsal': rehearsal,
    }
    return context
