from django.db import models

from apps.authentication.models.custom_user import CustomUser
from apps.library.choices import BookRate


class Book(models.Model):

    book_name = models.CharField(max_length=100)
    pages = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    rate = models.CharField(max_length=100, choices=BookRate.choices, default='NR')

    def __str__(self):
        return self.book_name