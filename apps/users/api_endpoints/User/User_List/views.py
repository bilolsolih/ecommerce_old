from rest_framework.generics import ListAPIView

from .serializers import UserListSerializer
from apps.users.models import User


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
