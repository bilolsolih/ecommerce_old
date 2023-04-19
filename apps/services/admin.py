from django.contrib import admin

from .models import Supplier, ShippingScope, DeliveryService

admin.site.register(Supplier)
admin.site.register(ShippingScope)
admin.site.register(DeliveryService)
