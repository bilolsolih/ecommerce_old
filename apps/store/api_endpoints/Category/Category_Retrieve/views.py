from rest_framework.generics import RetrieveAPIView

from .serializers import CategoryRetrieveSerializer
from ....models import Category


class CategoryRetrieveAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryRetrieveSerializer
