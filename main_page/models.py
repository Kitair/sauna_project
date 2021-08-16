from django.db import models
from uuid import uuid4
from os import path
from django.core.validators import RegexValidator


class Slider(models.Model):
    def get_file_name(self, filename):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/visit_slider', filename)

    title = models.CharField(unique=False, max_length=50)
    desc = models.CharField(max_length=500, unique=False)
    photo = models.ImageField(upload_to=get_file_name)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'


class About(models.Model):
    def get_file_name(self, filename):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/about', filename)

    photo = models.ImageField(upload_to=get_file_name)
    desc = models.CharField(max_length=150, unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.desc}'


class Offer(models.Model):
    def get_file_name(self, filename):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/offer', filename)

    photo = models.ImageField(upload_to=get_file_name)
    title = models.CharField(unique=True, max_length=50)
    desc = models.CharField(max_length=150, unique=True)
    price = models.CharField(unique=False, max_length=50)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'


class Events(models.Model):
    def get_file_name(self, filename):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/events', filename)

    photo = models.ImageField(upload_to=get_file_name)
    title = models.CharField(unique=True, max_length=50)
    desc = models.CharField(max_length=150, unique=True)
    price = models.CharField(unique=False, max_length=50)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'


class Feedback(models.Model):
    user_name = models.CharField(unique=True, max_length=30)
    quote = models.CharField(max_length=200, unique=True)
    is_visible = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user_name}'
