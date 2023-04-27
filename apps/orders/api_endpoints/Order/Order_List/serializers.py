from rest_framework.serializers import ModelSerializer

from apps.orders.models import Order


class OrderListSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['country']
