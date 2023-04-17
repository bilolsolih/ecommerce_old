from rest_framework.serializers import ModelSerializer

from ...Brand.Brand_Retrieve.serializers import BrandRetrieveSerializer
from ...Category.Category_Retrieve.serializers import CategoryRetrieveSerializer
from ....models import Item


class ItemListSerializer(ModelSerializer):
    category = CategoryRetrieveSerializer(many=False, read_only=True)
    brand = BrandRetrieveSerializer(many=False, read_only=True)

    class Meta:
        model = Item
        fields = "__all__"
