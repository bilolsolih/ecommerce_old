from rest_framework.generics import ListAPIView

from apps.services.api_endpoints.Supplier.Supplier_List.serializers import SupplierListSerializer
from apps.services.models import Supplier


class SupplierListAPIView(ListAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierListSerializer
