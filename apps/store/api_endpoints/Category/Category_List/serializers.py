from rest_framework.serializers import ModelSerializer

from ...Subcategory.Subcategory_Retrieve.serializers import SubcategoryRetrieveSerializer
from ....models import Category


class CategoryListSerializer(ModelSerializer):
    subcategories = SubcategoryRetrieveSerializer(many=True)

    class Meta:
        model = Category
        fields = '__all__'
