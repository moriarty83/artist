# Generated by Django 3.2.17 on 2023-03-05 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0009_alter_event_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
