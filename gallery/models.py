from django.db import models
from uuid import uuid4
from os import path


class Category(models.Model):
    title = models.CharField(unique=True, max_length=50)
    description = models.CharField(max_length=150, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_visible = models.BooleanField(default=True)
    is_sauna = models.BooleanField(default=False)
    is_vat = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'


class Gallery(models.Model):
    def get_file_name(self, filename):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/Gallery', filename)

    photo = models.ImageField(upload_to=get_file_name)
    is_visible = models.BooleanField(default=True)
    is_sauna = models.BooleanField(default=False)
    is_vat = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.photo}'
