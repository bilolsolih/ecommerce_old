from rest_framework.serializers import ModelSerializer

from apps.orders.models import Order


class OrderCreateSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['country', 'region', 'city', 'street', 'postal_code']
