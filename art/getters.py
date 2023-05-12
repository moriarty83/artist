from .models import Image, HeroImage, Event
from datetime import date


def getAllUpcomingEvents():
    today = date.today()
    earliest_event = Event.objects.earliest("event_start_date")
    latest_event = Event.objects.latest("event_start_date")

    upcoming_events = Event.objects.filter(
        ongoing_event=False, event_start_date__range=[today, latest_event.event_start_date]
    ).order_by("event_start_date")
    ongoing_events = Event.objects.filter(
        ongoing_event=True, event_end_date__range=[today, latest_event.event_start_date]
    ).order_by("event_end_date")
    past_events = Event.objects.filter(
        ongoing_event=True,
        event_end_date__range=[earliest_event.event_start_date, today],
    ).order_by("event_end_date")

    all_events = {
        "upcoming_events": upcoming_events,
        "ongoing_events": ongoing_events,
        "past_events": past_events,
    }
    return all_events