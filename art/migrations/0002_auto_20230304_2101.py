# Generated by Django 3.2.17 on 2023-03-05 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='name',
        ),
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(default=None, upload_to='images'),
        ),
        migrations.AddField(
            model_name='image',
            name='title',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
    ]
