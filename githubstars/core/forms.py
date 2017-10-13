from django import forms
from django.core.exceptions import ValidationError

from githubstars.core.validators import validate_unique_user


class RegisterForm(forms.Form):

    username = forms.CharField(label='Usuário', help_text='Utilize o mesmo usuário do github.',
                               validators=[validate_unique_user])
    password = forms.CharField(label='Senha', widget=forms.PasswordInput())
    password1 = forms.CharField(label='Repita a senha', widget=forms.PasswordInput())

    def clean(self):
        password = self.cleaned_data.get('password')
        password1 = self.cleaned_data.get('password1')

        if (password and password1) and (password != password1):
            raise ValidationError('Senhas não são iguais.')

        return self.cleaned_data
