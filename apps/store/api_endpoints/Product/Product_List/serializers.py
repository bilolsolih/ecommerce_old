from rest_framework.serializers import ModelSerializer

from ...Brand.Brand_Retrieve.serializers import BrandRetrieveSerializer
from ...Subcategory.Subcategory_Retrieve.serializers import SubcategoryRetrieveSerializer
from ....models import Product


class ProductListSerializer(ModelSerializer):
    category = SubcategoryRetrieveSerializer(read_only=True)
    brand = BrandRetrieveSerializer()

    class Meta:
        model = Product
        fields = ['title', 'brand', 'category', 'discount']
