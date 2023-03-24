from django.shortcuts import render, redirect
from django.template import loader
from django.views.generic import TemplateView, DetailView
from django.contrib.auth import authenticate, login

from .models import Image, HeroImage, Event

from django.http import HttpResponse
from datetime import date

from .forms import ImageForm
from django.shortcuts import get_list_or_404, get_object_or_404


# Create your views here.

############# USER VIEWS ################
class IndexView(TemplateView):
    today = date.today()
    year_later = date(today.year + 1, today.month, today.day)

    heroImage = HeroImage.objects.filter(homePage=True)[0]
    upcoming_events = Event.objects.filter(ongoing_event=False, event_start_date__range=[
                                           today, year_later]).order_by('event_start_date')[:3]
    ongoing_events = Event.objects.filter(ongoing_event=True, event_end_date__range=[
                                          today, year_later]).order_by('event_end_date')[:3]
    latest_image_list = Image.objects.order_by('created_at')[:5]
    context = {
        'latest_image_list': latest_image_list,
        'hero_image': heroImage,
        'upcoming_events': upcoming_events,
        'ongoing_events': ongoing_events
    }
    template_name = 'art/index.html'

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, self.context)


class PieceDetail(TemplateView):
    template_name = 'art/piece.html'

    def get(self, request, *args, **kwargs):
        image = get_object_or_404(Image, id=kwargs['id'])
        context = {'image': image}
        return render(request, self.template_name, context)


############# MANAGE VIEWS ################

class GalleryView(TemplateView):

    latest_image_list = Image.objects.order_by('created_at')[:5]
    context = {'latest_image_list': latest_image_list,
               'image_form': ImageForm(),
               'manage': False}
    template_name = 'art/gallery.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            print(request.user)
            self.context['manage'] = True
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

        return render(request, self.template_name)


# ACCOUNT

class LoginView(TemplateView):
    template_name = 'registration/login.html'
    context = {}

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, self.context)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return redirect('/')
            else:
                self.context = {'error': 'Account inactive'}
                return render(request, self.template_name, self.context)
        else:
            self.context = {'error': 'Invalid Login'}
            return render(request, self.template_name, self.context)
