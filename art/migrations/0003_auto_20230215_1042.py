# Generated by Django 3.2.17 on 2023-02-15 15:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0002_rename_images_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
