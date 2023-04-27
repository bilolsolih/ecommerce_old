from rest_framework.generics import RetrieveAPIView

from apps.services.api_endpoints.ExtraService.ExtraService_Retrieve.serializers import ExtraServiceRetrieveSerializer
from apps.services.models import ExtraService


class ExtraServiceRetrieveAPIView(RetrieveAPIView):
    queryset = ExtraService.objects.all()
    serializer_class = ExtraServiceRetrieveSerializer
