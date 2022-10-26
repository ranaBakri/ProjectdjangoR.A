from django import forms
from .models import Event


class EventItemForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["name", "image", "organiser", "available_seats",
                  "booked_seats", "date"]
