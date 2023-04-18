from rest_framework.generics import RetrieveAPIView

from .serializers import SubcategoryRetrieveSerializer
from ....models import Subcategory


class SubcategoryRetrieveAPIView(RetrieveAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategoryRetrieveSerializer
