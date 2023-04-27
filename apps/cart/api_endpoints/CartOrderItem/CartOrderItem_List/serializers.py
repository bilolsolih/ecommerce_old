from rest_framework.serializers import ModelSerializer

from apps.orders.models import CartOrderItem


class CartItemListSerializer(ModelSerializer):
    class Meta:
        model = CartOrderItem
        fields = ['product', 'delivery_service', 'quantity', 'price']
