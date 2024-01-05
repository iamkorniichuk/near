from django.urls import path

from .views import UserListView, UserDetailsView

app_name = "users"

urlpatterns = [
    path("", UserListView.as_view(), name="list"),
    path("<int:pk>/", UserDetailsView.as_view(), name="details"),
]
