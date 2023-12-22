import os
from tempfile import TemporaryDirectory

from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from django.conf import settings


class MediaTestCase(TestCase):
    def setUp(self):
        self.temp_dir = TemporaryDirectory()

    def tearDown(self):
        del self.temp_dir

    def test_valid_mime_type(self):
        files = [
            SimpleUploadedFile(
                "video.mp4",
                self.get_file_content("video.mp4"),
                content_type="video/mp4",
            ),
            SimpleUploadedFile(
                "image.png",
                self.get_file_content("image.png"),
                content_type="image/png",
            ),
            SimpleUploadedFile(
                "video", self.get_file_content("video.mp4"), content_type=""
            ),
            SimpleUploadedFile(
                "image.txt",
                self.get_file_content("image.png"),
                content_type="text/plain",
            ),
        ]
        for file in files:
            response = self.post_file(file)
            self.assertEqual(response.status_code, 201)

    def test_invalid_mime_type(self):
        files = [
            SimpleUploadedFile(
                "text.txt",
                self.get_file_content("text.txt"),
                content_type="text/plain",
            ),
            SimpleUploadedFile(
                "image.png",
                self.get_file_content("text.txt"),
                content_type="image/png",
            ),
            SimpleUploadedFile(
                "text", self.get_file_content("text.txt"), content_type=""
            ),
        ]
        for file in files:
            response = self.post_file(file)
            self.assertEqual(response.status_code, 400)

    def post_file(self, file):
        with self.settings(MEDIA_ROOT=self.temp_dir.name):
            return self.client.post(reverse("media-list"), {"file": file})

    def get_file_content(self, name):
        path = os.path.join(settings.MEDIA_ROOT, "test", name)
        with open(path, "rb") as file:
            return file.read()
