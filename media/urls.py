from django.urls import path

from .views import MediaDetailsView


app_name = "media"

urlpatterns = [
    path("<int:pk>/", MediaDetailsView.as_view(), name="details"),
]
