from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from django.views.generic import TemplateView, DetailView, UpdateView
from django.contrib.auth import authenticate, login

from .models import Image, HeroImage, Event
from .forms import ImageForm, EventForm

from django.http import HttpResponse
from datetime import date
from .getters import getAllUpcomingEvents


from .forms import ImageForm
from django.shortcuts import get_list_or_404, get_object_or_404


# Create your views here.


############# INDEX VIEW ################
class IndexView(TemplateView):
    template_name = "art/index.html"

    def get(self, request, *args, **kwargs):
        today = date.today()
        year_later = date(today.year + 1, today.month, today.day)

        heroImage = Image.objects.filter(home_page=True).order_by("created_at")[0]
        featured_events = Event.objects.filter(
            event_start_date__range=[today, year_later]
        ).order_by("event_start_date")[:3]
        featured_images = Image.objects.filter(featured=True).order_by("created_at")
        context = {
            "manage": False,
            "featured_images": featured_images,
            "hero_image": heroImage,
            "featured_events": featured_events,
        }
        if request.user.is_authenticated:
            context["manage"] = True

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            oldHeroImage = Image.objects.filter(home_page=True).order_by("created_at")[
                0
            ]
            oldHeroImage.home_page = False
            oldHeroImage.save(),

            newHero = get_object_or_404(Image, id=kwargs["id"])
            print(newHero)
            newHero.home_page = True
            newHero.save()
            self.context["hero_image"] = newHero
            self.context["featured_images"] = Image.objects.filter(
                featured=True
            ).order_by("created_at")

        return render(request, self.template_name, self.context)


###########################################
################ PIECES ###################
###########################################


############# GALLERY VIEW ################
class GalleryView(TemplateView):
    template_name = "art/gallery.html"

    def get(self, request, *args, **kwargs):
        latest_image_list = Image.objects.order_by("created_at")[:5]
        context = {
            "latest_image_list": latest_image_list,
            "image_form": ImageForm(),
            "manage": False,
        }
        print(context["image_form"])
        if request.user.is_authenticated:
            context["manage"] = True
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            print(form)
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            self.context["img_obj"] = img_obj

        return render(request, self.template_name, self.context)


# <form method='POST'>
#     {{form1.as_p}}
#     <button type="submit" name="btnform1">Save Changes</button>
#     </form>
#     <form method='POST'>
#     {{form2.as_p}}
#     <button type="submit" name="btnform2">Save Changes</button>
#     </form>
# if request.method=='POST' and 'btnform1' in request.POST:
#     do something...
# if request.method=='POST' and 'btnform2' in request.POST:
#     do something...

############# VIEW/UPDATE PIECE VIEW ################


class PieceDetail(TemplateView):
    template_name = "art/piece.html"

    def get(self, request, *args, **kwargs):
        image = get_object_or_404(Image, id=kwargs["id"])
        context = {"image": image, "manage": False}
        if request.user.is_authenticated:
            context["manage"] = True
            context["form"] = ImageForm(instance=image)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        print(args)
        print(kwargs)
        imageForm = ImageForm(request.POST or None)
        if imageForm.is_valid():
            image = get_object_or_404(Image, id=kwargs["id"])
            image.title = imageForm.cleaned_data.get("title")
            image.media = imageForm.cleaned_data.get("media")
            image.description = imageForm.cleaned_data.get("description")
            image.date = imageForm.cleaned_data.get("date")
            image.for_sale = imageForm.cleaned_data.get("for_sale")
            image.price = imageForm.cleaned_data.get("price")
            image.featured = imageForm.cleaned_data.get("featured")
            if imageForm.cleaned_data.get("image") != None:
                image.image = imageForm.cleaned_data.get("image")

            image.save()
            print(image.id)
        else:
            print("form invalid")
        return redirect("/art/gallery/{}".format(image.id))


###########################################
################ EVENTS ###################
###########################################


class EventsIndex(TemplateView):
    template_name = "art/events.html"

    def get(self, request, *args, **kwargs):
        context = {**getAllUpcomingEvents() }
        if request.user.is_authenticated:
            context["manage"] = True
            context["event_form"]= EventForm()
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = EventForm(request.POST, request.FILES)
        print(form)
        print(form.errors)

        if form.is_valid():
            print(form)
            form.save()
            # Get the current instance object to display in the template
            event_obj = form.instance
            self.context["event_obj"] = event_obj

        context = {**getAllUpcomingEvents() }
        if request.user.is_authenticated:
            context["manage"] = True
            context["event_form"]: EventForm()
        return render(request, self.template_name, context)

class EventDetail(TemplateView):
    template_name = "art/event.html"
    def get(self, request, *args, **kwargs):
        event = get_object_or_404(Event, id=kwargs["id"])
        context = {"event": event, "manage": False}
        if request.user.is_authenticated:
            context["manage"] = True
            context["form"] = EventForm(instance=event)

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        print(kwargs)
        eventForm = EventForm(request.POST or None)
        event = get_object_or_404(Event, id=kwargs["id"])

        print(eventForm.errors)
        if eventForm.is_valid():
            print("event form valid")
            event.event_name = eventForm.cleaned_data.get("event_name")
            event.description = eventForm.cleaned_data.get("description")
            event.featured = eventForm.cleaned_data.get("featured")
            event.ongoing_event = eventForm.cleaned_data.get("ongoing_event")
            event.event_start_date = eventForm.cleaned_data.get("event_start_date")
            event.event_time = eventForm.cleaned_data.get("event_time")
            event.event_end_date = eventForm.cleaned_data.get("event_end_date")
            event.event_address = eventForm.cleaned_data.get("event_address")
            event.event_city = eventForm.cleaned_data.get("event_city")
            event.event_state = eventForm.cleaned_data.get("event_state")
            event.event_zip = eventForm.cleaned_data.get("event_zip")
            event.save()
        else:
            print("form invalid")
        # event = get_object_or_404(Event, id=kwargs["id"])
        # context = {"event": event, "manage": False}
        # if request.user.is_authenticated:
        #     context["manage"] = True
        #     context["form"] = EventForm(instance=event)

        return redirect("/art/events/{}".format(event.id))

    ###########################################
    ################ ACCOUNT ###################
    ###########################################
    # ACCOUNT


class LoginView(TemplateView):
    template_name = "registration/login.html"
    context = {}

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, self.context)

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return redirect("/")
            else:
                self.context = {"error": "Account inactive"}
                return render(request, self.template_name, self.context)
        else:
            self.context = {"error": "Invalid Login"}
            return render(request, self.template_name, self.context)
