from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework.response import Response

from apps.common.models import BaseModel
from apps.orders.api_endpoints.OrderItem.OrderItem_List.serializers import OrderItemListSerializer


class Order(BaseModel):
    user = models.ForeignKey(
        verbose_name=_('User who made this order'),
        to='users.User',
        related_name='orders',
        on_delete=models.SET_NULL,
        null=True
    )
    postal_code = models.CharField(verbose_name=_('Postal code'), max_length=20)
    country = models.CharField(verbose_name=_('Country'), max_length=100)
    region = models.CharField(verbose_name=_('Region'), max_length=100)
    city = models.CharField(verbose_name=_('City'), max_length=100)
    street = models.CharField(verbose_name=_('Street'), max_length=100)

    coupon = models.ForeignKey(verbose_name=_('Coupon'), to='orders.Coupon', related_name='orders', on_delete=models.SET_NULL, null=True)
    price_before_discount = models.DecimalField(verbose_name=_('Price before discount'), max_digits=24, decimal_places=2, default=0)
    price_after_discount = models.DecimalField(verbose_name=_('Price after discount'), max_digits=24, decimal_places=2, default=0)

    paid = models.BooleanField(verbose_name=_('Paid'), default=False)

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    @property
    def get_items(self):
        items = self.items.all()
        serializer = OrderItemListSerializer(items, many=True)
        return Response(serializer.data)

    def clean_fields(self, exclude=None):
        if not self.user.cart.items.exists():
            raise ValidationError('The user\'s cart is empty, no need to create any orders!')
        super().clean_fields()
