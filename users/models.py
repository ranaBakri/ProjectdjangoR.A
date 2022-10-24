from django.db import models
from django.contrib.auth import get_user_model
# from datetime import date

User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.title
# class Event(models.Model):
#     Name = models.CharField(max_length=150)
#     image = models.ImageField()
#     organiser = models.CharField(max_length=150)
#     number_OfSeats = models.IntegerField()
#     number_OfBookSeats = models.IntegerField()
#     date_OfEvent = models.DateTimeField(auto_now_add=True)

# def __str__(self):
#     return self.organiser
