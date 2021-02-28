from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Event

def index(request):
    latest_event_list = Event.objects.order_by('-event_name')[:5]
    context = {'latest_event_list': latest_event_list}
    return render(request, 'assignments/index.html', context)

def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'assignments/detail.html', {'event': event})

def like(request, event_id):
    try:
	    event = get_object_or_404(Event, pk=event_id)
    except (KeyError, Event.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'assignments/detail.html', {
            'event': event,
            'error_message': "You didn't select a choice.",
        })
    else:
        event.is_liked = not event.is_liked
        event.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('assignments:index'))