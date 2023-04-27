from rest_framework import serializers

from apps.orders.models import OrderItem
from apps.store.api_endpoints.Product.Product_Retrieve.serializers import ProductRetrieveSerializer


class OrderItemListSerializer(serializers.ModelSerializer):
    product = ProductRetrieveSerializer(many=False, read_only=True)

    class Meta:
        model = OrderItem
        fields = ['product', 'quantity', 'delivery_service']
