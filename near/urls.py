from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from places.viewsets import PlaceViewSet

from .schema import schema_view

router = DefaultRouter()
router.register("places", PlaceViewSet, basename="place")

urlpatterns = (
    [
        path("", include(router.urls)),
        path("<str:app_label>/<int:object_id>/media/", include("media.urls")),
        path("tokens/", include("tokens.urls")),
        path("users/", include("users.urls")),
        path("profiles/", include("profiles.urls")),
        path("emails/", include("emails.urls")),
        path(
            "schema/",
            schema_view.with_ui(),
            name="schema",
        ),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
