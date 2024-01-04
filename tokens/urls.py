from django.urls import path

from .views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)

app_name = "tokens"

urlpatterns = [
    path("", TokenObtainPairView.as_view(), name="obtain"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("blacklist/", TokenBlacklistView.as_view(), name="blacklist"),
]
