from django.urls import reverse_lazy
from django.views.generic import CreateView
from rest_framework import generics

from users.forms import UserRegisterForm
from users.models import CustomUser
from users.serializers import UserSerializers


class RegisterUser(CreateView):
    model = CustomUser
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'
    extra_context = {
        'title': 'Регистрация'
    }


