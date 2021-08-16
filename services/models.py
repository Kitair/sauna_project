from django.db import models
from os import path


class Services(models.Model):
    title = models.CharField(unique=True, max_length=50)
    price = models.CharField(unique=False, max_length=50)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'
