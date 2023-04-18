from rest_framework.serializers import ModelSerializer

from ....models import Cart


class CartListSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
