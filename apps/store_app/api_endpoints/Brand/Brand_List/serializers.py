from rest_framework.serializers import ModelSerializer

from ....models import Brand


class BrandListSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = ['title', 'logo']
