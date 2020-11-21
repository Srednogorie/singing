import os

from django.db.models.signals import pre_save
from django.dispatch import receiver

from songs.models import CustomUser


@receiver(pre_save, sender=CustomUser)
def delete_old_file(sender, instance, **kwargs):
    # on creation, signal callback won't be triggered
    if instance._state.adding and not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).avatar
    except sender.DoesNotExist:
        return False

    # comparing the new file with the old one
    file = instance.avatar
    if not old_file == file:
        try:
            if os.path.isfile(old_file.path):
                os.remove(old_file.path)
        except ValueError:
            return False
