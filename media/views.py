from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.contenttypes.models import ContentType

from commons.mixins import PopulateDataMixin

from .serializers import MediaSerializer, MultipleMediaSerializer
from .models import Media, related_content_types


class ContentObjectViewMixin(PopulateDataMixin):
    def filter_queryset_by_content_object(self, app_label, object_id):
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

    def get_populated_data(self, *args, **kwargs):
        app_label = kwargs["app_label"]
        object_id = kwargs["object_id"]
        return self.get_content_object_data(app_label, object_id)


class MediaListView(ContentObjectViewMixin, ListCreateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    queryset = Media.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return MultipleMediaSerializer
        return MediaSerializer

    # TODO: To test on different endpoints in one run
    def list(self, request, app_label, object_id):
        self.queryset = self.filter_queryset_by_content_object(app_label, object_id)
        return super().list(request)


class MediaDetailsView(ContentObjectViewMixin, RetrieveUpdateDestroyAPIView):
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = MediaSerializer
    queryset = Media.objects.all()
