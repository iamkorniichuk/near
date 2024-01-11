from django.urls import reverse
from django.conf import settings
from rest_framework.test import APITestCase

from commons.files import FileManager


class MediaFileTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        cls.dir = FileManager(settings.SOURCE_MEDIA_ROOT, "rb")
        cls.dir.read_all()

    @classmethod
    def tearDownClass(cls):
        cls.dir.close_all()

    def post_media(self, **kwargs):
        return self.client.post(reverse("media-list"), kwargs)

    def delete_media(self, pk):
        return self.client.delete(reverse("media-detail", kwargs={"pk": pk}))

    def put_media(self, pk, **kwargs):
        return self.client.put(
            reverse("media-detail", kwargs={"pk": pk}),
            kwargs,
            "multipart",
        )

    def patch_media(self, pk, **kwargs):
        return self.client.patch(
            reverse("media-detail", kwargs={"pk": pk}),
            kwargs,
            "multipart",
        )
