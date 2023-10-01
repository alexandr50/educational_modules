from django.db import models

# Create your models here.
from django.db import models


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