from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel


# TODO thumbnail
class Supplier(BaseModel):
    title = models.CharField(verbose_name=_('Supplier name'), max_length=255)
    logo = models.ImageField(verbose_name=_('Supplier logo'), upload_to='images/services/logos/')
    country = models.ForeignKey(verbose_name=_('Country'), to='cities_light.Country', on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(verbose_name=_('City'), to='cities_light.City', on_delete=models.SET_NULL, null=True)
    is_verified = models.BooleanField(verbose_name=_('Is verified?'), default=False)
    shipping_scope = models.ForeignKey(
        verbose_name=_('Shipping scope'),
        to='services.ShippingScope',
        related_name='suppliers',
        on_delete=models.SET_NULL,
        null=True, blank=True
    )

    class Meta:
        verbose_name = _('Supplier')
        verbose_name_plural = _('Suppliers')

    def __str__(self):
        return f"Supplier {self.title}"


class ExtraService(BaseModel):
    title = models.CharField(verbose_name=_('Service name'), max_length=255)
    service_photo = models.ImageField(verbose_name=_('Service photo'), upload_to='images/services/service_photos/')
    service_icon = models.ImageField(verbose_name=_('Service icon'), upload_to='images/services/service_icons/')

    class Meta:
        verbose_name = _('Extra service')
        verbose_name_plural = _('Extra services')

    def __str__(self):
        return self.title


class DeliveryService(BaseModel):
    title = models.CharField(verbose_name=_('Delivery service name'), max_length=255)
    logo = models.ImageField(verbose_name=_('Delivery service logo'), upload_to='images/services/logos/', null=True, blank=True)

    # price_ranges

    class Meta:
        verbose_name = _('Delivery service')
        verbose_name_plural = _('Delivery services')


class PriceRange(BaseModel):
    service = models.ForeignKey(verbose_name=_('Related parent service'), to='services.DeliveryService', related_name='price_ranges', on_delete=models.CASCADE)
    quantity_from = models.DecimalField(verbose_name=_('Beginning from'), max_digits=24, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    quantity_to = models.DecimalField(verbose_name=_('To and including'), max_digits=24, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    price_per_unit = models.DecimalField(verbose_name=_('Price per kilometer'), max_digits=24, decimal_places=2, default=0, validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = _('Price range')
        verbose_name_plural = _('Price ranges')
        ordering = ['quantity_from']

    def clean_fields(self, exclude=None):
        if self.quantity_from >= self.quantity_to:
            raise ValidationError({"quantity_from": "Quantity 'Beginning from' should be smaller than quantity 'To and including'!"})
        super().clean_fields()

    def __str__(self):
        return f"Price range from {self.quantity_from} to {self.quantity_to}"


class ShippingScope(BaseModel):
    type = models.CharField(verbose_name=_('Shipping scope type'), max_length=255)

    class Meta:
        verbose_name = _('Shipping scope type')
        verbose_name_plural = _('Shipping scope types')
