from django.db.models import signals
from django.dispatch import receiver

from .models import Media


@receiver(signals.post_delete, sender=Media)
def delete_file_on_delete(sender, instance, **kwargs):
    delete_file(instance.file)


@receiver(signals.pre_save, sender=Media)
def delete_file_on_change(sender, instance, **kwargs):
    if instance.pk is None:
        return

    try:
        old_file = Media.objects.get(pk=instance.pk).file
    except Media.DoesNotExist:
        return

    new_file = instance.file
    if not old_file == new_file:
        delete_file(old_file)


def delete_file(file):
    if file:
        file.delete(save=False)
