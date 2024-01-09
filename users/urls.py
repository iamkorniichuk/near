from django.urls import path

from .views import UserCreateView, UserDetailsView

app_name = "users"

urlpatterns = [
    path("", UserCreateView.as_view(), name="create"),
    path("me/", UserDetailsView.as_view(), name="details"),
]
