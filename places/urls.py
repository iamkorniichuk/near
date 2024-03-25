from django.urls import path

from media.views import media_create_view_factory

from .models import Place


app_name = "places"

PlaceMediaView = media_create_view_factory(Place)

urlpatterns = [
    path("<int:pk>/media/", PlaceMediaView.as_view(), name="media"),
]
