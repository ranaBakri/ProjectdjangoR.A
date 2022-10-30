from dataclasses import field, fields
#from pyexpat import model
#from statistics import model
from django import forms
from .models import Event


class EventItemForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["name", "image", "available_seats",
                  "booked_seats", "date"]


class CreateEvent(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
