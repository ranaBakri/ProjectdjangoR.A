from django.db import models

# Create your models here.


class Event(models.Model):
    class EventKind(models.TextChoices):
        birthday = "Birthday"
        wedding = "Wedding"
        meeting = "Meeting"
        small_party = "SP"
        big_part = "Bp"
    name = models.CharField(max_length=150)
    image = models.ImageField(default="")
    organiser = models.CharField(max_length=150)
    number_OfSeats = models.IntegerField()
    number_OfBookSeats = models.IntegerField()
    date_OfEvent = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Admin(models.Model):
    aid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=20)


class Book_event(models.Model):
    bid = models.AutoField(primary_key=True)
    uid = models.IntegerField()
    name = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    mobile = models.CharField(max_length=10)


def __str__(self):
    return self.name
