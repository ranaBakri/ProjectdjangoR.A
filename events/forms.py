from django import forms
from .models import Event


class EventItemForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["name", "image", "organiser", "number_OfSeats",
                  "number_OfBookSeats", "date_OfEvent", "modified_at"]
