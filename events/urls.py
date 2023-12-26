from django.urls import path, re_path

from . import views as EventViews


urlpatterns = [
    path('', EventViews.event_page, name="event"),
]

