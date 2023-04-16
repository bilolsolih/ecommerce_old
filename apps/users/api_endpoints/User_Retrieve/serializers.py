from rest_framework.serializers import ModelSerializer

from ...models import User


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ['is_staff', 'is_active', 'is_superuser', 'groups', 'last_login', 'user_permissions']
