from django.shortcuts import render
from django.template import loader
from django.views.generic import TemplateView

from .models import Image

from django.http import HttpResponse

from google.cloud import storage

import json, requests


# Create your views here.

class IndexView(TemplateView):

    latest_image_list = Image.objects.order_by('-created_at')[:5]
    context = {
        'latest_image_list': latest_image_list,
    }
    template_name = 'art/index.html'


        
class ManageGalleryView(TemplateView):

    latest_image_list = Image.objects.order_by('-created_at')[:5]
    context = {
        'latest_image_list': latest_image_list,
    }
    template_name = 'manage/gallery.html'

    def get(self, request, *args, **kwargs):


        return render(request, self.template_name, {'context': self.context})
    

    def post(self, request, *args, **kwargs):
        print('post request')
        storage_client = storage.Client()
        bucket = storage_client.get_bucket('kcg-paint-images')
        path = "/Users/chrismoriarty/Downloads/b18e6ed1071bfada62ff7a6e829d7b25.jpeg" 
        blob = bucket.blob('gallery-images/zoidberg.jpg')
        blob.upload_from_filename(path)
        print(f"Bucket {blob} created.")
        return render(request, self.template_name, {'context': self.context})
        

class UploadView(TemplateView):
    template_name = 'manage/gallery.html'
    def get(self, request, *args, **kwargs):
        
        print("hello world")
        return render(request, self.template_name)


def detail(request, id):
    return HttpResponse("You're looking at imge %s." % id)
