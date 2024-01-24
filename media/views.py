from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.contenttypes.models import ContentType

from .serializers import MediaSerializer
from .models import Media, related_content_types


class ContentObjectViewMixin:
    def filter_queryset(self, app_label, object_id):
        filters = self.get_content_type_filters(app_label)
        return self.queryset.filter(object_id=object_id, **filters).all()

    def get_content_type_filters(self, app_label):
        return next(
            kwargs
            for kwargs in related_content_types
            if kwargs["app_label"] == app_label
        )

    def get_content_object_data(self, app_label, object_id):
        filters = self.get_content_type_filters(app_label)
        return {
            "content_type": ContentType.objects.get(**filters).pk,
            "object_id": object_id,
        }


class MediaListView(ListCreateAPIView, ContentObjectViewMixin):
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = MediaSerializer
    queryset = Media.objects.all()

    def list(self, request, app_label, object_id):
        self.queryset = self.filter_queryset(app_label, object_id)
        return super().list(request)

    def create(self, request, app_label, object_id):
        request.data.update(self.get_content_object_data(app_label, object_id))
        return super().create(request)


class MediaDetailsView(RetrieveUpdateDestroyAPIView, ContentObjectViewMixin):
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = MediaSerializer
    queryset = Media.objects.all()

    def update(self, request, app_label, object_id, *args, **kwargs):
        request.data.update(self.get_content_object_data(app_label, object_id))
        return super().update(request, app_label, object_id, *args, **kwargs)
