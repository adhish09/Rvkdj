# Generated by Django 4.1.7 on 2023-03-18 08:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0002_event_end_event_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='registrants',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
