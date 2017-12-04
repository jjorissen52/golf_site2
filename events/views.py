import datetime

from django.views.generic import TemplateView
from rest_framework import viewsets

from events.models import Event
from events.serializers import EventSerializer

class UpcomingEventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.filter(start__gt=datetime.datetime.now())
    serializer_class = EventSerializer

class PastEventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.filter(start__lt=datetime.datetime.now())
    serializer_class = EventSerializer

class UpcomingCalendarView(TemplateView):
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        kwargs.update(super(UpcomingCalendarView, self).get_context_data(**kwargs))
        kwargs["events"] = Event.objects.filter(start__gt=datetime.datetime.now()).values('title', 'start', 'end', 'description', 'id')
        kwargs["api_url"] = "upcoming-list"
        kwargs["title_mod"] = "Upcoming"
        return kwargs

class PastCalendarView(TemplateView):
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        kwargs.update(super(PastCalendarView, self).get_context_data(**kwargs))
        kwargs["events"] = Event.objects.filter(start__lt=datetime.datetime.now()).values('title', 'start', 'end', 'description', 'id')
        kwargs["api_url"] = "past-list"
        kwargs["title_mod"] = "Past"
        return kwargs