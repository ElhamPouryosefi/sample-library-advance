from django.db import models


class BookRate(models.TextChoices):
    good = 'g'
    medium = 'm'
    bad = 'b'
    not_rated = 'nr'
