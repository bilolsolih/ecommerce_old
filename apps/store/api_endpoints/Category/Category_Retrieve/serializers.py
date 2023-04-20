from rest_framework.serializers import ModelSerializer

from ...Subcategory.Subcategory_Retrieve.serializers import SubcategoryRetrieveSerializer
from ....models import Category


# TODO create a separate serializer to be used as nested with fewer fields

class CategoryRetrieveSerializer(ModelSerializer):
    subcategories = SubcategoryRetrieveSerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'title', 'slug', 'subcategories']
