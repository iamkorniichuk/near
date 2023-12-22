from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser

from .serializers import MediaSerializer
from .models import Media


class MediaViewSet(ModelViewSet):
    parser_classes = [MultiPartParser, FormParser]
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
