from tempfile import TemporaryDirectory
import os

from .settings import *


SOURCE_MEDIA_ROOT = os.path.join(MEDIA_ROOT, "test")
MEDIA_ROOT = TemporaryDirectory().name

REST_FRAMEWORK = {
    **REST_FRAMEWORK,
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"],
}
