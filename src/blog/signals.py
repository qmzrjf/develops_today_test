from django.db.models.signals import post_save
from django.dispatch import receiver

from blog.models import Post


@receiver(post_save, sender=Post)
def save_file(sender, instance, created, **kwargs):
    if created:
        instance.link = "/".join(["post", str(instance.id)])
        instance.save()
