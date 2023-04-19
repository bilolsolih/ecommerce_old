from rest_framework import serializers

from ....models import CartEntry


class CartEntryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartEntry
        fields = ['product', 'delivery_service', 'quantity']
