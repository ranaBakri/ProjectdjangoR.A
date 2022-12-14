# from unicodedata import name
from django.shortcuts import render, redirect
from .forms import LoginForm, NewUserForm, BookEventForm
from django.contrib.auth import authenticate, login, logout
from events.models import Event
from users.models import BookEvent
# from django.http import Http404
# from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(request, "home.html")


def user_register(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            print("VALID")
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            login(request, user)
            return redirect("home")

    return render(request=request, template_name="user_register.html", context={"form": form})


def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect("home")
    context = {"form": form}
    return render(request, "login.html", context)


def logout_request(request):
    logout(request)

    return redirect("login")


def book_event(request, event_id):
    event = Event.objects.get(id=event_id)
    form = BookEventForm()
    if request.method == "POST":
        form = BookEventForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.participint = request.user
            booking.event = event
            booking.save()
            return redirect("Done")

    context = {
        "form": form,
        "event": {
            "id": event_id,
        }
    }
    return render(request, 'eventBooking.html', context)
