from django.shortcuts import render
from django.template import loader
from django.views.generic import TemplateView

from .models import Image

from django.http import HttpResponse

from .Google import Create_Service

# Create your views here.

API_NAME = 'photoslibrary'
API_VERSION = 'v1'
CLIENT_SECRET_FILE = 'client_secret_googlephotos.json'
SCOPES=[
    'https://www.googleapis.com/auth/photoslibrary'
]

class IndexView(TemplateView):
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

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


def detail(request, id):
    return HttpResponse("You're looking at imge %s." % id)
