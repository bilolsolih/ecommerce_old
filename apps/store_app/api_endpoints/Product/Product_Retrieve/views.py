from rest_framework.generics import RetrieveAPIView

from .serializers import ProductRetrieveSerializer
from ....models import Product


class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductRetrieveSerializer
