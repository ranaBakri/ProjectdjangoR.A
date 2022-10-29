
from random import choices
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Event(models.Model):
    class EventKind(models.TextChoices):
        birthday = "Birthday"
        wedding = "Wedding"
        meeting = "Meeting"
        small_party = "SP"
        big_part = "Bp"
    name = models.CharField(max_length=150, choices=EventKind.choices)
    image = models.ImageField()
    organiser = models.ForeignKey(User, on_delete=models.CASCADE)
    available_seats = models.PositiveIntegerField()
    booked_seats = models.PositiveIntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return self.name
    # modified_at = models.DateTimeField(auto_now=True)


# class Admin(models.Model):
#     aid = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=20)
#     email = models.CharField(max_length=40)
#     password = models.CharField(max_length=20)
