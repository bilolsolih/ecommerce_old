from rest_framework.serializers import ModelSerializer

from ....models import Brand


class BrandRetrieveSerializer(ModelSerializer):
    model = Brand
    fields = ['title']
