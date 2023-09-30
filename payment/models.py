from django.db import models


class Payment(models.Model):
    is_done = models.BooleanField(default=False, verbose_name='Оплачено')
    user = models.ForeignKey('users.CustomUser',
                                on_delete=models.CASCADE,
                                verbose_name='покупатель')
    educational_module = models.ForeignKey('educational_modules.EducationalModule',
                                              on_delete=models.CASCADE,
                                              verbose_name='Образовательный модуль')


    def __str__(self):
        return f'{self.user} | {self.educational_module}'


    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'