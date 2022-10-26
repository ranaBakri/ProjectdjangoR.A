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
