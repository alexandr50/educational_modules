from django import forms

from bank_card.models import BankCard


class BankCardForm(forms.ModelForm):
    csv = forms.CharField(widget=forms.PasswordInput(), label='csv')

    def __init__(self, *args, **kwargs):
        super(BankCardForm, self).__init__(*args, **kwargs)
        # self.fields['csv'].widget.attrs['hidden'] = True
        for field_name, field in self.fields.items():
             field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = BankCard
        fields = ('number_card', 'date', 'csv')



