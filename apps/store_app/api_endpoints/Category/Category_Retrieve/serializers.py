from rest_framework.serializers import ModelSerializer

from ....models import Category


class CategoryRetrieveSerializer(ModelSerializer):
    model = Category
    fields = ['title']
