from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404,
)
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.contenttypes.models import ContentType

from commons.mixins import PopulateCreateDataMixin, PopulateUpdateDataMixin
from profiles.permissions import IsOwnerOrReadOnly

from .serializers import MediaSerializer, MultipleMediaSerializer
from .models import Media


class MediaDetailsView(PopulateUpdateDataMixin, RetrieveUpdateDestroyAPIView):
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = MediaSerializer
    queryset = Media.objects.all()

    def get_permissions(self):
        return super().get_permissions() + [IsOwnerOrReadOnly("content_object.profile")]

    def perform_destroy(self, instance):
        filters = {
            "content_type": instance.content_type,
            "object_id": instance.object_id,
            "order__gt": instance.order,
        }
        instance.delete()
        queryset = self.get_queryset()
        next_media = queryset.filter(**filters).order_by("order").all()
        for media in next_media:
            media.order -= 1
        queryset.bulk_update(next_media, ["order"])

    def get_populated_data(self):
        instance = self.get_object()

        return {
            "content_type": instance.content_type.pk,
            "object_id": instance.object_id,
        }


def media_create_view_factory(model):
    class MediaCreateView(GenericMediaCreateView):
        content_type_pk = ContentType.objects.get_for_model(model).pk

    return MediaCreateView


class GenericMediaCreateView(PopulateCreateDataMixin, CreateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    queryset = Media.objects.all()
    content_type_pk = None

    def get_serializer_class(self):
        if self.request.method == "POST":
            return MultipleMediaSerializer
        return MediaSerializer

    def get_permissions(self):
        return super().get_permissions() + [IsOwnerOrReadOnly("profile")]

    def get_populated_data(self):
        return {"content_type": self.content_type_pk, "object_id": self.kwargs["pk"]}

    def create(self, request, *args, **kwargs):
        filters = self.get_populated_data()
        Model = ContentType.objects.get_for_id(filters["content_type"]).model_class()
        obj = get_object_or_404(Model.objects.all(), **{"pk": filters["object_id"]})

        self.check_object_permissions(self.request, obj)
        return super().create(request, *args, **kwargs)
