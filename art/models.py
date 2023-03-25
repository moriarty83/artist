from django.db import models

# Create your models here.


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images', default=None, blank=True)
    description = models.TextField(blank=True)
    date = models.DateField(blank=True)
    for_sale = models.BooleanField(blank=True)
    sold = models.BooleanField(blank=True)
    price = models.IntegerField(blank=True)
    featured = models.BooleanField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class HeroImage(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images', default=None)
    description = models.TextField(blank=True)
    homePage = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Event(models.Model):
    event_name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images', default=None)
    ongoing_event = models.BooleanField(default=False)
    event_start_date = models.DateField()
    event_time = models.TimeField()
    event_end_date = models.DateField(blank=True, null=True)
    event_address = models.CharField(max_length=200)
    event_city = models.CharField(max_length=30)
    event_state = models.CharField(max_length=20)
    event_zip = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event_name
