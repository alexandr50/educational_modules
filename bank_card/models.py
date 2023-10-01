from django.db import models
from .validators import validate_card_number

class BankCard(models.Model):
    number_card = models.CharField(max_length=19, verbose_name='Номер карты', validators=[validate_card_number])
    date = models.CharField(max_length=5, verbose_name='Дата')
    csv = models.IntegerField(verbose_name='csv')
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, verbose_name='владелец')


    def __str__(self):
        return f'{self.number_card[:4]}*************{self.number_card[-3:-1]}'

    class Meta:
        verbose_name = 'Банковская карта'
        verbose_name_plural = 'Банковские карты'
