from rest_framework import serializers

from apps.orders.models import CartItem


class CartItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ["delivery_service", "quantity"]
