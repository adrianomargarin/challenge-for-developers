from model_mommy import mommy
from django.shortcuts import resolve_url
from githubstars.core.tests.mixins import BaseTest


class HomeTest(BaseTest):

    def setUp(self):
        self.login()

        repository = mommy.make('core.Repository', user=self.user, name='Nome', url='http://github.com',
                                language='Python', tags='python, django')

        self.response = self.client.get(resolve_url('home'))

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        """Must use base.html"""
        self.assertTemplateUsed(self.response, 'base.html')
