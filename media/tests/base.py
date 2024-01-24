from django.urls import reverse
from django.conf import settings
from django.contrib.gis.geos import Point
from rest_framework.test import APITestCase

from commons.files import FileManager
from places.models import Place
from users.models import User
from profiles.models import Profile


class MediaFileTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        cls.dir = FileManager(settings.SOURCE_MEDIA_ROOT, "rb")
        cls.dir.read_all()

        cls.user, _ = User.objects.get_or_create(
            email="test@gmail.com", password="12345678"
        )
        cls.profile, _ = Profile.objects.get_or_create(
            {
                "user": cls.user,
                "name": "test",
            }
        )
        cls.place, _ = Place.objects.get_or_create(
            {
                "name": "test",
                "description": "test",
                "location": Point(0, 0),
                "profile": cls.profile,
            }
        )

    @classmethod
    def tearDownClass(cls):
        cls.dir.close_all()

    def post_media(self, **data):
        return self.client.post(
            reverse(
                "media:list",
                kwargs={
                    "app_label": "places",
                    "object_id": self.place.pk,
                },
            ),
            data,
        )

    def delete_media(self, pk):
        return self.client.delete(
            reverse(
                "media:details",
                kwargs={"app_label": "places", "object_id": self.place.pk, "pk": pk},
            )
        )

    def put_media(self, pk, **data):
        return self.client.put(
            reverse(
                "media:details",
                kwargs={"app_label": "places", "object_id": self.place.pk, "pk": pk},
            ),
            data,
            "multipart",
        )

    def patch_media(self, pk, **data):
        return self.client.patch(
            reverse(
                "media:details",
                kwargs={"app_label": "places", "object_id": self.place.pk, "pk": pk},
            ),
            data,
            "multipart",
        )
