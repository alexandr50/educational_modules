from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=30, verbose_name='название')


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'