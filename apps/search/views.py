from elasticsearch_dsl import Q
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.search.documents.products import CategoryDocument, ProductDocument
from apps.search.serializers import SearchProductCategorySerializer
from apps.store.api_endpoints.Product.Product_List.serializers import \
    ProductListSerializer


class SearchProductCategoryAPIView(APIView):
    search_document = CategoryDocument
    serializer_class = SearchProductCategorySerializer

    def get(self, request, query, *args, **kwargs):
        try:
            q = Q("multi_match", query=query, fields=["title"], fuzziness="AUTO")
            search = self.search_document.search().query(q)
            serializer = self.serializer_class(search.to_queryset(), many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=500)


class SearchProductAPIView(APIView):
    search_document = ProductDocument
    serializer_class = ProductListSerializer

    def get(self, request, query, *args, **kwargs):
        try:
            q = Q("multi_match", query=query, fields=["title"], fuzziness="AUTO")
            search = self.search_document.search().query(q)
            serializer = self.serializer_class(search.to_queryset(), many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
