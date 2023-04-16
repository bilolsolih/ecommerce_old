from rest_framework.generics import DestroyAPIView

from apps.common.permissions import IsTheSameUser
from ...models import User


class UserDestroyAPIView(DestroyAPIView):
    permission_classes = [IsTheSameUser]
    queryset = User.objects.all()
