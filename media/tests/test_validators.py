from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status

from .base import MediaFileTestCase


class MimeTypeValidatorTestCase(MediaFileTestCase):
    def test_valid_mime_type(self):
        files = [
            SimpleUploadedFile(
                "video.mp4",
                self.dir.contents["video.mp4"],
                content_type="video/mp4",
            ),
            SimpleUploadedFile(
                "image.png",
                self.dir.contents["image.png"],
                content_type="image/png",
            ),
            SimpleUploadedFile(
                "video", self.dir.contents["video.mp4"], content_type=""
            ),
            SimpleUploadedFile(
                "image.txt",
                self.dir.contents["image.png"],
                content_type="text/plain",
            ),
        ]
        response = self.post_media(files=files)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_mime_type(self):
        files = [
            SimpleUploadedFile(
                "text.txt",
                self.dir.contents["text.txt"],
                content_type="text/plain",
            ),
            SimpleUploadedFile(
                "image.png",
                self.dir.contents["text.txt"],
                content_type="image/png",
            ),
            SimpleUploadedFile("text", self.dir.contents["text.txt"], content_type=""),
        ]
        response = self.post_media(files=files)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
