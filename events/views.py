from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from events import models
from events.forms import EventItemForm


# Create your views here.


def get_event(request):
    events = event.objects.all()
    new_event = []
    for event in events:
        eve = {
            "name": event.name,
            "image": event.image,
            "organiser": event.organiser,
            "number_OfSeats": event.number_OfSeats,
            "number_OfBookSeats": event.number_OfBookSeats,
            "date_OfEvent": event.date_OfEvent,
        }
        new_event.append(eve)

    context = {"event": new_event}
    return render(request, "event-list.html", context)


def create_event_item(request):
    form = EventItemForm.object()
    context = {"form": form}
    return render(request, 'create_event.html', context)
