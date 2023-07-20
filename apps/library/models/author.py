
from django.db import models

from apps.authentication.models.custom_user import CustomUser


class Author(models.Model):
    name = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True)
    death_date = models.DateField(null=True)

    def __str__(self):
        return self.name
