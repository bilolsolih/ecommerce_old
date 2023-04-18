from rest_framework.generics import ListAPIView

from .serializers import CategoryListSerializer
from ....models import Category


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    http_method_names = ['GET']
