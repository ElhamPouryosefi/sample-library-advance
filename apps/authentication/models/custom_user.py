from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUser(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    country = models.CharField(max_length=30, default='iran')
    phone_number = models.PositiveIntegerField(default=0)
    is_author = models.BooleanField(default=False)

    objects = UserManager()

    def __str__(self):
        self.username
