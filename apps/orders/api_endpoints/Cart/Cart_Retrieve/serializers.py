from rest_framework.serializers import ModelSerializer

from apps.orders.models import Cart


class CartRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"
