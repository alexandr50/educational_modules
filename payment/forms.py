from django import forms

# from educational_modules.models import EducationalModule
from payment.models import Payment
from users.models import CustomUser


class PayFormModule(forms.ModelForm):
    # number_card = forms.CharField(max_length=20, required=True,
    #                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Банковская карта'}))
    #
    # user = forms.CharField(initial='none', max_length=20)
    # educational_module = forms.CharField(max_length=20)
    # def __init__(self, *args, **kwargs):
    #
    #     super(PayFormModule, self).__init__(*args, **kwargs)
    #     self.initial = self.user
    #     self.fields['user'].widget.attrs['readonly'] = True
    #     self.fields['educational_module'].widget.attrs['readonly'] = True
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Payment
        fields = ('user', 'educational_module')
