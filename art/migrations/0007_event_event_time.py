# Generated by Django 3.2.17 on 2023-03-05 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0006_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_time',
            field=models.TimeField(default='09:00'),
            preserve_default=False,
        ),
    ]
