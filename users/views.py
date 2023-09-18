from django.shortcuts import render
from django.views.generic import CreateView
from rest_framework import generics

from users.forms import UserRegisterForm
from users.models import CustomUser
from users.serializers import UserSerializers


class RegisterUser(CreateView):
    model = CustomUser
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    extra_context = {
        'title': 'Регистрация'
    }

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



