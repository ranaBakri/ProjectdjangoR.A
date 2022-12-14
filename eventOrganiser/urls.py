"""eventOrganiser URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from turtle import done
from django.contrib import admin
from django.urls import path
from events.models import Event
from users.models import BookEvent
from users.views import user_register, home, login_view, logout_request, book_event
from events.views import delete_event, get_events, Done, delete_event, create_event_item
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", user_register, name="register"),
    path("home/", home, name="home"),
    path("login/", login_view, name="login"),
    path("logout/", logout_request, name="logout"),
    path("events/", get_events, name="event-list"),
    path("Done/", Done, name="Done"),
    path("booking/<int:event_id>/", book_event, name="bookEvent"),
    path("add/createevent/",
         create_event_item, name="createevent"),
    path("delete/createevent/", delete_event, name="delete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
