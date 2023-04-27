from rest_framework import serializers

from apps.orders.models import CartOrderItem


class CartItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartOrderItem
        fields = ["delivery_service", "quantity"]
