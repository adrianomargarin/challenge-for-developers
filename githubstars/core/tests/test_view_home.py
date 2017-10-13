from model_mommy import mommy
from django.shortcuts import resolve_url
from githubstars.core.tests.mixins import BaseTest


class HomeTest(BaseTest):

    def setUp(self):
        self.login()

        repository = mommy.make('core.Repository', user=self.user, name='Nome', url='http://github.com',
                                language='Python')
        repository.tags.add(mommy.make('core.Tag', name='python'))
        repository.tags.add(mommy.make('core.Tag', name='django'))

        self.response = self.client.get(resolve_url('home'))

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        """Must use base.html"""
        self.assertTemplateUsed(self.response, 'base.html')

    def test_html(self):
        tags = (
            ('<table', 1),
            ('<thead', 1),
            ('<tbody', 1),
            ('<th>Nome</th>', 1),
            ('<th>URl</th>', 1),
            ('<th>Linguagem</th>', 1),
            ('<th>Tags</th>', 1),
            ('<td>Nome', 1),
            ('<td><a href="http://github.com"', 1),
            ('<td>Python', 1),
            ('<td>python, django', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)
