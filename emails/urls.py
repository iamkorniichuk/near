from django.urls import path

from .views import ConfirmConfirmationCodeView

app_name = "emails"

urlpatterns = [
    path("confirm/", ConfirmConfirmationCodeView.as_view(), name="confirm"),
]
