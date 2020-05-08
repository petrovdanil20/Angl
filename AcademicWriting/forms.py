from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from AcademicWriting.models import Essay

class EssayCheckForm(forms.Form):
    text = forms.CharField(label="Text", widget=forms.Textarea(attrs={'rows': '20', 'class':'form-control'}))

class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class EssayForm(forms.ModelForm):
    class Meta:
        model = Essay
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control mb-3'