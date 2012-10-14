#encoding: utf-8
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('is_staff', 'is_active', 'is_superuser', 'date_joined', 'groups', 'user_permissions', 'password')

class PasswordReset(forms.Form):
    oldpassword = forms.CharField(max_length=200, label='Senha Atual', widget=forms.PasswordInput)
    password1 = forms.CharField(max_length=200, label='Nova Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=200, label='Confirme', widget=forms.PasswordInput)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(PasswordReset, self).__init__(*args, **kwargs)

    def clean_oldpassword(self):
        if self.cleaned_data.get('oldpassword') and not self.user.check_password(self.cleaned_data['oldpassword']):
            raise ValidationError('Digite a senha Atual')
        return self.cleaned_data['oldpassword']

    def clean_password2(self):
        if self.cleaned_data.get('password1') and self.cleaned_data.get('password2') and self.cleaned_data['password1'] != self.cleaned_data['password2']:
            raise ValidationError('As senhas não são as mesmas')
        return self.cleaned_data['password2']
    
        