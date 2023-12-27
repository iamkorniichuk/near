from django.core.files import File
from django.core.files.uploadedfile import SimpleUploadedFile

from media.models import Media

from .base import MediaFileTestCase


class FileRemovalTestCase(MediaFileTestCase):
    def setUp(self):
        self.media = Media.objects.create(file=File(self.dir["image.png"]))
        self.storage = self.media.file.storage
        self.old_file = self.media.file

    def assert_old_file_removal(self):
        self.assertFalse(self.storage.exists(self.old_file.name))

    def test_file_removal_on_delete(self):
        self.delete_media(self.media.pk)
        self.assert_old_file_removal()

    def test_file_removal_on_patch(self):
        file = SimpleUploadedFile(
            "video.mp4", self.dir.contents["video.mp4"], "video/mp4"
        )
        self.patch_media(self.media.pk, file=file)
        self.assert_old_file_removal()

    def test_file_removal_on_put(self):
        file = SimpleUploadedFile(
            "video.mp4", self.dir.contents["video.mp4"], "video/mp4"
        )
        self.put_media(self.media.pk, file=file)
        self.assert_old_file_removal()
