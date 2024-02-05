from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.contenttypes.models import ContentType
from copy import copy

from commons.mixins import PopulateDataMixin

from .serializers import MediaSerializer, MultipleMediaSerializer
from .models import Media


"""
POST: events/13/media/ -> append multiple media with continuous `order` to this model
DELETE: media/<pk>/ -> delete certain media shifting `order`
PATCH: events/13/media/ -> change order of this model's media 
"""


class MediaDeleteView(DestroyAPIView):
    queryset = Media.objects.all()


def media_create_view_factory(model):
    class MediaCreateView(GenericMediaCreateView):
        content_type_pk = ContentType.objects.get_for_model(model).pk

    return MediaCreateView


class GenericMediaCreateView(PopulateDataMixin, CreateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    queryset = Media.objects.all()
    content_type_pk = None

    def get_serializer_class(self):
        if self.request.method == "POST":
            return MultipleMediaSerializer
        return MediaSerializer

    def get_populated_data(self, pk):
        print(ContentType.objects.get(pk=self.content_type_pk).model, pk)
        return {"content_type": self.content_type_pk, "object_id": pk}
