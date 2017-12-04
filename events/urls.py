from django.conf.urls import url

from events import views

urlpatterns = [
    url(r'^upcoming/$', views.UpcomingCalendarView.as_view(), name='upcoming'),
    url(r'^past/$', views.PastCalendarView.as_view(), name='past'),
]