from django.db import models
from os import path
from django.core.validators import RegexValidator


class Booking(models.Model):
    mobile_regex = RegexValidator(regex=r'(\d{3}[- .]?){2}\d{4}$', message='Phone in format xxx xxx xxxx')

    service_field = models.CharField(max_length=5)
    date_field = models.CharField(max_length=10)
    time_field = models.CharField(max_length=5)
    is_processed = models.BooleanField(default=False)
    order_time = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(max_length=30)
    user_phone = models.CharField(max_length=13, validators=[mobile_regex])

    def __str__(self):
        return f'{self.service_field}: {self.date_field} на {self.time_field}'


