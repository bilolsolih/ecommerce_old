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
    shipping_scope = models.CharField(verbose_name=_('Shipping scope'), max_length=255)

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
    title = models.CharField(verbose_name=_('Service name'), max_length=255)

    # TODO

    class Meta:
        verbose_name = _('Delivery service')
        verbose_name_plural = _('Delivery services')
