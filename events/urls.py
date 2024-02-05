from django.urls import path

from media.views import media_create_view_factory

from .models import Event


app_name = "events"

EventMediaView = media_create_view_factory(Event)

urlpatterns = [
    path("<int:pk>/media/", EventMediaView.as_view(), name="media"),
]
