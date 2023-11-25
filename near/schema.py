from django.utils.translation import gettext_lazy as _

from drf_yasg.views import get_schema_view
from drf_yasg.openapi import Info


schema_view = get_schema_view(
    Info(
        title=_("near"),
        default_version="v0.0.0",
    ),
)
