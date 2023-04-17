from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel


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

    class Meta:
        verbose_name = _('Delivery service')
        verbose_name_plural = _('Delivery services')
