from rest_framework.serializers import ModelSerializer
from ....models import Subcategory

class SubcategoryListSerializer(ModelSerializer):
    class Meta:
        model = Subcategory
        fields = '__all__'