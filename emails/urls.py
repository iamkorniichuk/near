from django.urls import path

from .views import VerifyEmailView

app_name = "emails"

urlpatterns = [
    path("verify-email/", VerifyEmailView.as_view(), name="verify-email"),
]
