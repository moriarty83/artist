from django import forms
from .models import Image, Event


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image', 'media', 'description', 'date',
                  'for_sale', 'sold', 'price', 'featured')


class EventForm(forms.ModelForm):
    """Form for the event model"""
    class Meta:
        model = Event
        fields = ('event_name', 'description', 'image', 'ongoing_event', 'event_start_date',
                  'event_time', 'event_end_date', 'event_address', 'event_city', 'event_state', 'event_zip')
