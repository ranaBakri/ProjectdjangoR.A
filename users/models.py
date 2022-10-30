
from django.db import models
from django.contrib.auth import get_user_model
from events.models import Event
# from datetime import date

User = get_user_model()


# class Post(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=50)
#     content = models.TextField()

#     def __str__(self):
#         return self.title


class BookEvent(models.Model):
    # user = models.ForeignKey(
    # User, on_delete=models.CASCADE)
    numbers_of_seats = models.PositiveIntegerField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    participint = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.participint.name} has booked '
