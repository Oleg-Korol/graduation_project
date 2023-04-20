from uuid import uuid4

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile


@receiver(post_save,sender = User, dispatch_uid = uuid4())
def create_profile_handler(sender,instance,created,**kwargs):
    if created :
        UserProfile.objects.create(user = instance)


