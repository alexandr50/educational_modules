from django.db import models

from users.models import CustomUser


class EducationalModule(models.Model):
    category = models.ForeignKey('categories.Category', on_delete=models.SET_NULL, verbose_name='Категория', null=True)
    name = models.CharField(max_length=30, verbose_name='Название')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    description = models.TextField(verbose_name='Описание')
    price = models.PositiveIntegerField(default=0, verbose_name='Стоимость')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Образовательный модуль'
        verbose_name_plural = 'Образовательные модули'


class UserModule(models.Model):
    educational_module = models.ForeignKey('educational_modules.EducationalModule', on_delete=models.CASCADE, verbose_name='Модуль')
    custom_user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, verbose_name='Пользователь')


    def __str__(self):
        return f'{self.educational_module.name} | {self.custom_user.email}'


