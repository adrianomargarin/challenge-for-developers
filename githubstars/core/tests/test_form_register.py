from model_mommy import mommy
from django.test import TestCase

from githubstars.core.forms import RegisterForm


class RegisterTestCase(TestCase):

    def test_form_has_fields(self):
        form = RegisterForm()
        expected = ['username', 'password', 'password1']

        self.assertSequenceEqual(expected, list(form.fields))

    def test_username_unique(self):
        mommy.make('auth.User', username='adrianomargarin')
        form = self.make_validated_form()

        self.assertEqual(form.errors['username'], ['Já existe um usuário com esse username.'])

    def test_password_not_equal_password1(self):
        form = self.make_validated_form(password1='87654321')

        self.assertEqual(form.errors['__all__'], ['Senhas não são iguais.'])

    def make_validated_form(self, **kwargs):
        valid = {
            'username': 'adrianomargarin',
            'password': '12345678',
            'password1': '12345678'
        }

        data = dict(valid, **kwargs)
        form = RegisterForm(data)
        form.is_valid()

        return form
