from django.db import models


class Payment(models.Model):
    is_done = models.BooleanField(default=False, verbose_name='Оплачено')
    user = models.OneToOneField('users.CustomUser',
                                on_delete=models.CASCADE,
                                verbose_name='покупатель')
    educational_module = models.OneToOneField('educational_modules.EducationalModule',
                                              on_delete=models.CASCADE,
                                              verbose_name='Образовательный модуль')
