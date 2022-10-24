from django.db import models


class user(models.Model):
    Name = models.CharField(max_length=150)
    Age = models.IntegerField()
    is_staff = models.BooleanField()
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    last_login = models.DateField("Date", auto_now_add=True)
