from rest_framework.serializers import ModelSerializer

from apps.services.models import DeliveryService


class DeliveryServiceListSerializer(ModelSerializer):
    class Meta:
        model = DeliveryService
        fields = ['title', 'logo']
