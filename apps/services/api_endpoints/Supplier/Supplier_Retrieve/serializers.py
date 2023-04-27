from rest_framework.serializers import ModelSerializer

from apps.services.models import Supplier


class SupplierRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'
