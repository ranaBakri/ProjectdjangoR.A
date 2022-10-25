from contextlib import redirect_stderr
from email import message
import http
from http.client import HTTPResponse
from django.http import HttpRequest
from pyexpat.errors import messages
from django.shortcuts import render, redirect
from .forms import LoginForm, NewUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

from django.http import Http404


def home(request: HttpRequest) -> HTTPResponse:
    return render(request, "home.html")


def user_register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful")
            return redirect("home")
        messages.error(
            request, "Unsuccessful registration invalid informations")
    form = NewUserForm()
    return render(request=request, template_name="user_register.html", context={"Register": form})


def login(request):
    form = LoginForm(request.POST)
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect("home/")
    context = {"LoginForm": form}
    return render(request, "login.html", context)


def logout_request(request):
    logout(request)

    messages.info(request, "you have successfully logged out")
    return redirect("login/")


def permission(request):
    if request.user.is_anonymous:
        return redirect("login")
    elif not request.user.is_staff:
        raise Http404
