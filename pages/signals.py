from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from .models import Profile
User = get_user_model()


@receiver(post_save, sender=User, dispatch_uid='create_user')
def create_user(*args, **kwargs):
    obj = kwargs.get("instance")

    # code
    if Profile.objects.filter(user=obj).last():
        pass
    else:
        Profile.objects.create(user=obj)