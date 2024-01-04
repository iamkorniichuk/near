from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from media.viewsets import MediaViewSet

from .schema import schema_view

router = DefaultRouter()
router.register("media", MediaViewSet, basename="media")

urlpatterns = (
    [
        path("", include(router.urls)),
        path(
            "schema/",
            schema_view.with_ui(),
            name="schema",
        ),
        path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
        path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
