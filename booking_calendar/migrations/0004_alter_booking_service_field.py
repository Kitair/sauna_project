# Generated by Django 3.2.6 on 2021-09-16 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_calendar', '0003_alter_booking_service_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='service_field',
            field=models.CharField(choices=[('Сауна', 'Сауна'), ('Чан', 'Чан')], default='Сауна', max_length=5),
        ),
    ]
