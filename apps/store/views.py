from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Category, Product
from .serializers import CategorySerializer


class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


