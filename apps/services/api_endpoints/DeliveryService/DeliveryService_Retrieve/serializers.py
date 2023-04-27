from rest_framework.serializers import ModelSerializer

from apps.services.models import DeliveryService


class DeliveryServiceRetrieveSerializer(ModelSerializer):
    class Meta:
        model = DeliveryService
        fields = ['title', 'logo']
