from rest_framework import serializers

from ....models import CartEntry


class CartEntryRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartEntry
        fields = ['product', 'delivery_service', 'quantity']
