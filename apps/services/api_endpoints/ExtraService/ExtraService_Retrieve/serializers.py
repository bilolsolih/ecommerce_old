from rest_framework.serializers import ModelSerializer

from apps.services.models import ExtraService


class ExtraServiceRetrieveSerializer(ModelSerializer):
    class Meta:
        model = ExtraService
        fields = ['title', 'service_photo', 'service_icon']
