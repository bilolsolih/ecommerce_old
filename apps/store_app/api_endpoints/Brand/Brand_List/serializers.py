from rest_framework.serializers import ModelSerializer

from ....models import Brand


class BrandListSerializer(ModelSerializer):
    model = Brand
    fields = ['title']
