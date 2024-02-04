from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.contenttypes.models import ContentType

from commons.mixins import PopulateCreateDataMixin, PopulateUpdateDataMixin

from .serializers import MediaSerializer, MultipleMediaSerializer
from .models import Media


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
