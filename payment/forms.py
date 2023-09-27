from django import forms

from educational_modules.models import EducationalModule


class PyaFormModule(forms.ModelForm):
    class Meta:
        model = EducationalModule
        fields = '__all__'
