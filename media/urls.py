from django.urls import path

from .views import MediaListView, MediaDetailsView


app_name = "media"

urlpatterns = [
    path(
        "",
        MediaListView.as_view(),
        name="list",
    ),
    path(
        "<int:pk>/",
        MediaDetailsView.as_view(),
        name="details",
    ),
]
