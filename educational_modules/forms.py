from django import forms

from educational_modules.models import EducationalModule


class EdModuleForm(forms.ModelForm):

    class Meta:
        model = EducationalModule
        fields = ('name',)

    def __init__(self, *args, **kwargs):
        super(EdModuleForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['readonly'] = True
