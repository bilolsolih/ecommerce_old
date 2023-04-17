from rest_framework.generics import RetrieveAPIView

from .serializers import BrandRetrieveSerializer
from ....models import Brand


class BrandRetrieveAPIView(RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandRetrieveSerializer
