from rest_framework.serializers import ModelSerializer

from ...Brand.Brand_Retrieve.serializers import BrandRetrieveSerializer
from ...Category.Category_Retrieve.serializers import CategoryRetrieveSerializer
from ....models import Product


class ProductListSerializer(ModelSerializer):
    category = CategoryRetrieveSerializer(many=False, read_only=True)
    brand = BrandRetrieveSerializer(many=False, read_only=True)

    class Meta:
        model = Product
        fields = ['title', 'brand', 'category']
