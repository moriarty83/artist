from django import forms
from .models import Image


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('id', 'title', 'image', 'description', 'date',
                  'for_sale', 'sold', 'price', 'featured')
