from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.views.generic import TemplateView, DetailView, UpdateView
from django.contrib.auth import authenticate, login

from .models import Image, HeroImage, Event
from .forms import ImageForm, EventForm

from django.http import HttpResponse
from datetime import date

from .forms import ImageForm
from django.shortcuts import get_list_or_404, get_object_or_404


# Create your views here.

############# INDEX VIEW ################
class IndexView(TemplateView):
    template_name = 'art/index.html'

    today = date.today()
    year_later = date(today.year + 1, today.month, today.day)

    heroImage = HeroImage.objects.filter(homePage=True)[0]
    upcoming_events = Event.objects.filter(ongoing_event=False, event_start_date__range=[
                                           today, year_later]).order_by('event_start_date')[:3]
    ongoing_events = Event.objects.filter(ongoing_event=True, event_end_date__range=[
                                          today, year_later]).order_by('event_end_date')[:3]
    featured_images = Image.objects.filter(
        featured=True).order_by('created_at')
    context = {
        'featured_images': featured_images,
        'hero_image': heroImage,
        'upcoming_events': upcoming_events,
        'ongoing_events': ongoing_events
    }

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, self.context)

###########################################
################ PIECES ###################
###########################################


############# GALLERY VIEW ################
class GalleryView(TemplateView):

    latest_image_list = Image.objects.order_by('created_at')[:5]
    context = {'latest_image_list': latest_image_list,
               'image_form': ImageForm(),
               'manage': False}
    template_name = 'art/gallery.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
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


############# VIEW/UPDATE PIECE VIEW ################


class PieceDetail(TemplateView):
    template_name = 'art/piece.html'

    def get(self, request, *args, **kwargs):
        image = get_object_or_404(Image, id=kwargs['id'])
        context = {'image': image,
                   'manage': False}
        if request.user.is_authenticated:
            context['manage'] = True
            context['form'] = ImageForm(instance=image)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        print(args)
        print(kwargs)
        imageForm = ImageForm(request.POST or None)
        if imageForm.is_valid():
            image = get_object_or_404(Image, id=kwargs['id'])
            image.title = imageForm.cleaned_data.get('title')
            image.media = imageForm.cleaned_data.get('media')
            image.description = imageForm.cleaned_data.get('description')
            image.date = imageForm.cleaned_data.get('date')
            image.for_sale = imageForm.cleaned_data.get('for_sale')
            image.price = imageForm.cleaned_data.get('price')
            image.featured = imageForm.cleaned_data.get('featured')
            if imageForm.cleaned_data.get('image') != None:
                image.image = imageForm.cleaned_data.get('image')

            image.save()
            print(image.id)
        else:
            print("form invalid")
        return redirect('/art/gallery/{}'.format(image.id))

###########################################
################ EVENTS ###################
###########################################


class EventsIndex(TemplateView):
    template_name = 'art/events.html'

    today = date.today()

    def get(self, request, *args, **kwargs):
        year_later = date(self.today.year + 1,
                          self.today.month, self.today.day)
        earliest_event = Event.objects.earliest('event_start_date')

        upcoming_events = Event.objects.filter(ongoing_event=False, event_start_date__range=[
            self.today, year_later]).order_by('event_start_date')
        ongoing_events = Event.objects.filter(ongoing_event=True, event_end_date__range=[
            self.today, year_later]).order_by('event_end_date')
        past_events = Event.objects.filter(ongoing_event=True, event_end_date__range=[
            earliest_event.event_start_date, self.today]).order_by('event_end_date')

        context = {
            'upcoming_events': upcoming_events,
            'ongoing_events': ongoing_events,
            'past_events': past_events
        }
        return render(request, self.template_name, context)


class EventDetail(TemplateView):
    template_name = 'art/event.html'

    def get(self, request, *args, **kwargs):
        event = get_object_or_404(Event, id=kwargs['id'])
        context = {'event': event,
                   'manage': False}
        if request.user.is_authenticated:
            context['manage'] = True
            context['form'] = EventForm(instance=event)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        eventForm = EventForm(request.POST or None)
        if eventForm.is_valid():
            event = get_object_or_404(Event, id=kwargs['id'])
            event.event_name = eventForm.cleaned_data.get('event_name')
            event.description = eventForm.cleaned_data.get('description')
            event.ongoing_event = eventForm.cleaned_data.get('ongoing_event')
            event.event_start_date = eventForm.cleaned_data.get(
                'event_start_date')
            event.event_time = eventForm.cleaned_data.get('event_time')
            event.event_end_date = eventForm.cleaned_data.get('event_end_date')
            event.event_address = eventForm.cleaned_data.get('event_address')
            event.event_city = eventForm.cleaned_data.get('event_city')
            event.event_state = eventForm.cleaned_data.get('event_state')
            event.event_zip = eventForm.cleaned_data.get('event_zip')

            if eventForm.cleaned_data.get('image') != None:
                event.image = eventForm.cleaned_data.get('image')

            event.save()

        else:
            print("form invalid")
        return redirect('/art/gallery/{}', event.id)

    ###########################################
    ################ ACCOUNT ###################
    ###########################################
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
