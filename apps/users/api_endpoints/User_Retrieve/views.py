from rest_framework.generics import RetrieveAPIView

from .serializers import UserDetailSerializer
from ...models import User


class UserRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
