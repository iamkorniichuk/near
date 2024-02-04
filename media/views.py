from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.status import HTTP_201_CREATED
from django.contrib.contenttypes.models import ContentType
from django.utils.decorators import method_decorator

from drf_yasg.utils import swagger_auto_schema

from commons.mixins import PopulateCreateDataMixin, PopulateUpdateDataMixin

from .serializers import (
    MediaSerializer,
    MultipleMediaSerializer,
    SwaggerMultipleMediaSerializer,
)
from .models import Media


@method_decorator(
    name="post",
    decorator=swagger_auto_schema(
        request_body=SwaggerMultipleMediaSerializer(),
        responses={HTTP_201_CREATED: SwaggerMultipleMediaSerializer()},
    ),
)
class MediaListView(PopulateCreateDataMixin, ListCreateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    queryset = Media.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return MultipleMediaSerializer
        return MediaSerializer

    def get_populated_data(self, *args, **kwargs):
        content_type = ContentType.objects.get(model=self.request.data["model"])
        return {"content_type": content_type.pk}


class MediaDetailsView(PopulateUpdateDataMixin, RetrieveUpdateDestroyAPIView):
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = MediaSerializer
    queryset = Media.objects.all()

    def get_populated_data(self, *args, **kwargs):
        model = self.request.data.get("model", None)
        if model:
            content_type = ContentType.objects.get(model=model)
            return {"content_type": content_type.pk}
        return {}
