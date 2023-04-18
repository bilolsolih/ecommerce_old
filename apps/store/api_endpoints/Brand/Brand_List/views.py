from rest_framework.generics import ListAPIView

from .serializers import BrandListSerializer
from ....models import Brand


class BrandListAPIView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer
