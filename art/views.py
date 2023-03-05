from django.shortcuts import render
from django.template import loader
from django.views.generic import TemplateView

from .models import Image

from django.http import HttpResponse

from google.cloud import storage

from .forms import ImageForm

import json, requests


# Create your views here.

class IndexView(TemplateView):

    latest_image_list = Image.objects.order_by('created_at')[:5]
    context = {
        'latest_image_list': latest_image_list,
    }
    template_name = 'art/index.html'


        
class ManageGalleryView(TemplateView):

    latest_image_list = Image.objects.order_by('created_at')[:5]
    context = {'latest_image_list': latest_image_list, 'image_form': ImageForm()}
    template_name = 'manage/gallery.html'

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, self.context)
    

    def post(self, request, *args, **kwargs):
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            print(form)
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            self.context['img_obj'] = img_obj

        return render(request, self.template_name, self.context)
        

class UploadView(TemplateView):
    template_name = 'manage/gallery.html'
    def get(self, request, *args, **kwargs):
        
        print("hello world")
        return render(request, self.template_name)


def detail(request, id):
    return HttpResponse("You're looking at imge %s." % id)
