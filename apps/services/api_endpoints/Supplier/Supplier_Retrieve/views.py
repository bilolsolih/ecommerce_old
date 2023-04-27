from rest_framework.generics import RetrieveAPIView

from apps.services.api_endpoints.Supplier.Supplier_Retrieve.serializers import SupplierRetrieveSerializer
from apps.services.models import Supplier


class SupplierRetrieveAPIView(RetrieveAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierRetrieveSerializer
