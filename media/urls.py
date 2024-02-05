from django.urls import path

from .views import MediaDeleteView


app_name = "media"

urlpatterns = [
    path("<int:pk>/", MediaDeleteView.as_view(), name="delete"),
]
