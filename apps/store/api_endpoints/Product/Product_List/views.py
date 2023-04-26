from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.openapi import IN_QUERY, TYPE_STRING, Parameter
from drf_yasg.utils import swagger_auto_schema
from elasticsearch_dsl import Q
from rest_framework.generics import ListAPIView

from apps.search.documents.products import ProductDocument
from apps.store.api_endpoints.Product.Product_List.filters import ProductFilter

from ....models import Product
from .serializers import ProductListSerializer


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    search_document = ProductDocument

    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    # Todo rating and Features model

    @swagger_auto_schema(
        manual_parameters=[Parameter("q", IN_QUERY, description="Search term", type=TYPE_STRING)],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        search_query = self.request.query_params.get("q", None)

        if search_query:
            q = Q("multi_match", query=search_query, fields=["title"], fuzziness="AUTO")
            search = self.search_document.search().query(q)
            queryset = search.to_queryset()
            return queryset

        return self.queryset
