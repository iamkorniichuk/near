from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .schema import schema_view

urlpatterns = [
    path(
        "schema/",
        schema_view.with_ui(),
        name="schema",
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
