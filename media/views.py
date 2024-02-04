from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import MultiPartParser, FormParser

from .serializers import MediaSerializer, MultipleMediaSerializer
from .models import Media


class MediaListView(ListCreateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    queryset = Media.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return MultipleMediaSerializer
        return MediaSerializer


class MediaDetailsView(RetrieveUpdateDestroyAPIView):
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = MediaSerializer
    queryset = Media.objects.all()
