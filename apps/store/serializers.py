from rest_framework.serializers import ModelSerializer

from .api_endpoints.Subcategory.Subcategory_Retrieve.serializers import SubcategoryRetrieveSerializer
from .models import Category


class CategorySerializer(ModelSerializer):
    subcategories = SubcategoryRetrieveSerializer(many=True)

    class Meta:
        model = Category
        fields = '__all__'
