from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel


class Cart(BaseModel):
    user = models.OneToOneField(verbose_name=_('Customer'), to='users.User', related_name='cart', on_delete=models.CASCADE)
    # entries


class CartEntry(BaseModel):
    cart = models.ForeignKey(verbose_name=_('Cart'), to='cart.Cart', related_name='entries', on_delete=models.CASCADE)

    item = models.ForeignKey(
        verbose_name=_('Item name'),
        to='store.Item',
        related_name='cart_entries',
        on_delete=models.SET_NULL,
        null=True
    )
    quantity = models.PositiveIntegerField(verbose_name=_('Quantity'), default=0)

    class Meta:
        verbose_name = _('Cart entry')
        verbose_name_plural = _('Cart entries')
