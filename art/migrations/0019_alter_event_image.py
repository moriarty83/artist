# Generated by Django 3.2.18 on 2023-05-10 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0018_event_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, default=None, upload_to='images'),
        ),
    ]
