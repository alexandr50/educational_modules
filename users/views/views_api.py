from rest_framework import generics

from users.models import CustomUser
from users.serializers import UserSerializers


class UserListApiView(generics.ListAPIView):
    serializer_class = UserSerializers
    queryset = CustomUser.objects.all()


class UserCreateApiView(generics.CreateAPIView):
    serializer_class = UserSerializers
    queryset = CustomUser.objects.all()


class UserUpdateApiView(generics.UpdateAPIView):
    serializer_class = UserSerializers
    queryset = CustomUser.objects.all()


class UserRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = UserSerializers
    queryset = CustomUser.objects.all()


class UserDeleteApiView(generics.DestroyAPIView):
    serializer_class = UserSerializers
    queryset = CustomUser.objects.all()
