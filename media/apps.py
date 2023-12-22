from django.apps import AppConfig


class MediaConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "media"

    def ready(self):
        from .handlers import delete_file_on_delete, delete_file_on_change

        return super().ready()
