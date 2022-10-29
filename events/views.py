
from django.shortcuts import render, redirect
from events.models import Event
from events.forms import EventItemForm


# Create your views here.

def Done(request):
    return render(request, "Done.html")


def get_events(request):
    events = Event.objects.all()
    new_event = []
    for event in events:
        eve = {
            "name": event.name,
            "image": event.image,
            "organiser": event.organiser,
            "available_seats": event.available_seats,
            "booked_seats": event.booked_seats,
            "date": event.date,
        }
        new_event.append(eve)

    context = {"events": new_event}
    return render(request, "event-list.html", context)


def create_event_item(request):
    form = EventItemForm()
    if request.method == "POST":
        print("post")
        form = EventItemForm(request.POST, request.FILES)
        if form.is_valid():
            print("valid")
            form.save()
            return redirect("event_list")
    context = {"form": form}
    return render(request, 'create_event.html', context)


def update_event(request, event_id):
    event = Event.objects.get(id=event_id)
    form = EventItemForm(instance=event)
    if request.method == "POST":
        form = EventItemForm(request.POST, instance=Event)
        if form.is_valid():
            form.save()
            return redirect("event_list")
    context = {
        "event": event,
        "form": form,
    }

    return render(request, 'create_event', context)


def delete_event(request, event_id):
    Event.objects.get(id=event_id).delete()
    return redirect("event_list")
