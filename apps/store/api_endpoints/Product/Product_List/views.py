from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView

from apps.store.api_endpoints.Product.Product_List.filters import ProductFilter
from .serializers import ProductListSerializer
from ....models import Product


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_class = ProductFilter
    search_fields = ["category", "brand", "condition"]
    # Todo rating and Features model
