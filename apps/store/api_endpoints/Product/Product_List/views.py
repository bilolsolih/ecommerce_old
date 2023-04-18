from rest_framework.generics import ListAPIView

from .serializers import ProductListSerializer
from ....models import Product


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
