from django.urls import path

from .views import ConfirmCodeView

app_name = "emails"

urlpatterns = [
    path("confirm/", ConfirmCodeView.as_view(), name="confirm"),
]
