from rest_framework.generics import ListAPIView

from apps.services.api_endpoints.DeliveryService.DeliveryService_List.serializers import DeliveryServiceListSerializer
from apps.services.models import DeliveryService


class DeliveryServiceListAPIView(ListAPIView):
    queryset = DeliveryService.objects.all()
    serializer_class = DeliveryServiceListSerializer
