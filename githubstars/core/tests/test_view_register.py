from model_mommy import mommy
from django.test import TestCase
from django.shortcuts import resolve_url


class RegisterGetTest(TestCase):

    def setUp(self):
        self.response = self.client.get(resolve_url('register'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'register.html')

    # def test_html(self):
    #     tags = (
    #         ('<form', 1),
    #         ('<input', 2),
    #         ('type="text"', 1),
    #         ('type="password"', 2),
    #         ('type="submit"', 1)
    #     )
    #     for text, count in tags:
    #         with self.subTest():
    #             self.assertContains(self.response, text, count)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')


class RegisterPostValidTest(TestCase):

    def test_post(self):
        data = {
            'username': 'newuser',
            'password': '1234@asdf',
            'password1': '1234@asdf'
        }
        response = self.client.post(resolve_url('register'), data=data)

        self.assertEqual(302, response.status_code)


class RegisterPostInvalidTest(TestCase):

    def test_post(self):
        response = self.client.post(resolve_url('register'), data={})

        self.assertEqual(200, response.status_code)
