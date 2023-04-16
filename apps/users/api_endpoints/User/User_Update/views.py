from rest_framework import status
from rest_framework.generics import UpdateAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from apps.common.permissions import IsTheSameUser
from apps.users.models import User
from .serializers import UserUpdateSerializer


class UserUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [IsTheSameUser]
    parser_classes = [MultiPartParser, FormParser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            vd = serializer.validated_data
            username = vd['username']
            password = vd['password']
            phone_number = vd['phone_number']
            email = vd['email']
            first_name = vd['first_name']
            last_name = vd['last_name']
            gender = vd['gender']

            user = User.objects.create(
                username=username,
                phone_number=phone_number,
                email=email,
                first_name=first_name,
                last_name=last_name,
                gender=gender
            )
            user.set_password(password)
            user.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
