from django import forms

from .models import Image, Event


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 300px;'}))
        model = Image
        fields = ('title', 'image', 'media', 'description', 'date',
                  'for_sale', 'sold', 'price', 'featured')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'flex flex-row space-x-4 mb-6'}),
            'image': forms.ClearableFileInput(attrs={'class': 'flex flex-row space-x-4 mb-6'}),
            'media': forms.TextInput(attrs={'class': 'flex flex-row space-x-4 mb-6'}),
            'description': forms.Textarea(attrs={'rows': '4', 'cols':'50', 'class': 'flex flex-row space-x-4 mb-6'}),
            'date': forms.DateInput(attrs={'class': 'flex flex-row space-x-4 mb-6'}),
            'for_sale': forms.CheckboxInput(attrs={'class': 'flex flex-row space-x-4 mb-6'}),
            'sold': forms.CheckboxInput(attrs={'class': 'flex flex-row space-x-4 mb-6'}),
            'price': forms.NumberInput(attrs={'class': 'flex flex-row space-x-4 mb-6'}),
            'featured': forms.CheckboxInput(attrs={'class': 'flex flex-row space-x-4 mb-6'}),
        }

class EventForm(forms.ModelForm):
    """Form for the event model"""
    class Meta:
        model = Event
        fields = ('event_name', 'description', 'image', 'ongoing_event', 'event_start_date',
                  'event_time', 'event_end_date', 'event_address', 'event_city', 'event_state', 'event_zip')
