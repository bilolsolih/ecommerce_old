from rest_framework.serializers import ModelSerializer

from ...Brand.Brand_Retrieve.serializers import BrandRetrieveSerializer
from ...Category.Category_Retrieve.serializers import CategoryRetrieveSerializer
from ....models import Product


class ProductRetrieveSerializer(ModelSerializer):
    category = CategoryRetrieveSerializer()
    brand = BrandRetrieveSerializer()

    # TODO supplier uchun serializer qilib nested serializer sifatida olib kelish
    class Meta:
        model = Product
        fields = [
            'category',
            'brand',
            'supplier',
            'title',
            'price_per_unit',
            'get_ranges',
            'initial_quantity',
            'sold_quantity',
            'condition',
            'description',
            'created',
            'updated'
        ]
