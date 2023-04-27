from rest_framework.serializers import ModelSerializer

from apps.services.models import Supplier


class SupplierListSerializer(ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'
