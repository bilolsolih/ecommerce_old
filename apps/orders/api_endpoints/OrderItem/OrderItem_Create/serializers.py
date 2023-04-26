from rest_framework import serializers

from apps.orders.models import CartItem


class CartEntryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ["product", "delivery_service", "quantity"]
