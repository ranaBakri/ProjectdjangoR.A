from django import forms
from .models import User, BookEvent
from events.models import Event
from django.contrib.auth.forms import UserCreationForm


class NewUserForm(forms.ModelForm):
    # user should enter his email to make sign up
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password")


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())


class BookEventForm(forms.ModelForm):
    class Meta:
        model = BookEvent
        fields = ["numbers_of_seats", "event", "participint"]
