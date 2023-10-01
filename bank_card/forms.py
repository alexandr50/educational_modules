from django import forms

from bank_card.models import BankCard


class BankCardForm(forms.ModelForm):
    class Meta:
        model = BankCard
        fields = ('number_card', 'date', 'csv')
