from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter

from .serializers import ProductListSerializer
from ....models import Product


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = [SearchFilter]
    search_fields = ['category', 'brand', 'condition']
    # Todo rating and Features model
