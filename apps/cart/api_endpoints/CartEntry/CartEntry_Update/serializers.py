from rest_framework import serializers

from ....models import CartEntry


class CartEntryUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartEntry
        fields = ['delivery_service', 'quantity']
