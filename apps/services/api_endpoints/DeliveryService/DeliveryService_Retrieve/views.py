from rest_framework.generics import RetrieveAPIView

from apps.services.api_endpoints.DeliveryService.DeliveryService_Retrieve.serializers import DeliveryServiceRetrieveSerializer
from apps.services.models import DeliveryService


class DeliveryServiceRetrieveAPIView(RetrieveAPIView):
    queryset = DeliveryService.objects.all()
    serializer_class = DeliveryServiceRetrieveSerializer
