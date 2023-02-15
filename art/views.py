from django.shortcuts import render
from django.template import loader

from .models import Image

from django.http import HttpResponse
# Create your views here.

def index(request):
    latest_image_list = Image.objects.order_by('-created_at')[:5]
    template = loader.get_template('art/index.html')
    context = {
        'latest_image_list': latest_image_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, id):
    return HttpResponse("You're looking at imge %s." % id)
