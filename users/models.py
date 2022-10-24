from django.db import models
from django.contrib.auth.models import User
from datetime import date

class user(models.Model):
    Name = models.CharField(max_length=150)
    Age = models.IntegerField()
    is_staff = models.BooleanField()
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    last_login = models.DateField("Date", auto_now_add=True)

class Event(models.Model):
    Name = models.CharField(max_length=150)
    image = models.ImageField()
    organiser=models.CharField(max_length=150)
    NumberOfSeats=models.IntegerField()
    NumberOfBookSeats=models.IntegerField()
    DateOfEvent=models.DateTimeField(auto_now_add=True)