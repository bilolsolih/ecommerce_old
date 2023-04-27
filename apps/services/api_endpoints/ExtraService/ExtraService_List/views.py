from rest_framework.generics import ListAPIView

from apps.services.api_endpoints.ExtraService.ExtraService_List.serializers import ExtraServiceListSerializer
from apps.services.models import ExtraService


class ExtraServiceListAPIView(ListAPIView):
    queryset = ExtraService.objects.all()
    serializer_class = ExtraServiceListSerializer
