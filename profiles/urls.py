from django.urls import path

from .views import ProfileListView, ProfileDetailsView, MyProfileDetailsView


app_name = "profiles"

urlpatterns = [
    path("", ProfileListView.as_view(), name="list"),
    path("<int:pk>/", ProfileDetailsView.as_view(), name="details"),
    path("me/", MyProfileDetailsView.as_view(), name="my-details"),
]
