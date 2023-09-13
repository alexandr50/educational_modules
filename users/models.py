from django.db import models
from django.contrib.auth.models import AbstractUser
from educational_modules.models import EducationalModule


class CustomUser(AbstractUser):
    username = None
    first_name = models.CharField(max_length=20, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    age = models.PositiveIntegerField(verbose_name='Возраст', blank=True, null=True)
    email = models.EmailField(max_length=40, unique=True, verbose_name='Почта')
    educational_modules = models.ManyToManyField(EducationalModule)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
