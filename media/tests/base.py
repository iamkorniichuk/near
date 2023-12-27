import os
from tempfile import TemporaryDirectory

from django.urls import reverse
from rest_framework.test import APITestCase

from commons.settings import RestorableSettings
from commons.files import FileManager


class MediaFileTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp_dir = TemporaryDirectory()
        cls.conf = RestorableSettings(MEDIA_ROOT=cls.temp_dir.name)

        dir_path = os.path.join(cls.conf["MEDIA_ROOT"], "test")
        cls.dir = FileManager(dir_path, "rb")
        cls.dir.read_all()

    @classmethod
    def tearDownClass(cls):
        cls.temp_dir.cleanup()
        cls.conf.restore_all()
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
