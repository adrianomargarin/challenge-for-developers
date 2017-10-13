from model_mommy import mommy
from django.test import TestCase
from django.shortcuts import resolve_url


class LoginGetTest(TestCase):

    def setUp(self):
        self.response = self.client.get(resolve_url('login'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'login.html')

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')


class LoginPostTest(TestCase):

    def setUp(self):
        user = mommy.make('auth.User', username='adrianomargarin')
        user.set_password('12345678')
        user.save()
        data = {
            'username': user.username,
            'password': '12345678'
        }
        self.response = self.client.post(resolve_url('login'), data=data)

    def test_redirect(self):
        self.assertEqual(302, self.response.status_code)
