from rest_framework.serializers import ModelSerializer

from apps.services.models import ExtraService


class ExtraServiceListSerializer(ModelSerializer):
    class Meta:
        model = ExtraService
        fields = ['title', 'service_photo', 'service_icon']
