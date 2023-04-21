from rest_framework.serializers import ModelSerializer

from apps.orders.models import CartItem


class CartItemListSerializer(ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['the_product', 'delivery_service', 'quantity', 'price']
