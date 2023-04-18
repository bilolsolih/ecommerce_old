from rest_framework.generics import ListAPIView

from .serializers import SubcategoryListSerializer
from ....models import Subcategory


class SubcategoryListAPIView(ListAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategoryListSerializer
