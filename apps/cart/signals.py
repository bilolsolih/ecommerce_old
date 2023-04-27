from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.users.models import User

from .models import Cart


@receiver(post_save, sender=User)
def create_cart_for_new_user(sender, instance, **kwargs):
    Cart.objects.update_or_create(user=instance)
