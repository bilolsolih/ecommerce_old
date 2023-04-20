from rest_framework import serializers

from apps.orders.models import CartEntry


class CartEntryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartEntry
        fields = ["product", "delivery_service", "quantity"]
