from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    def clean_qq(self):
        clean_data = self.cleaned_data['qq']
        if not clean_data.isdigit():
            raise forms.ValidationError('纯数字')
        return int(clean_data)

    class Meta:
        model = Student
        fields = (
            'name','sex','qq',
            'email'
        )