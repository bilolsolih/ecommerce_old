from rest_framework.serializers import ModelSerializer


from ....models import Category


class CategoryListSerializer(ModelSerializer):
    model = Category
    fields = '__all__'
