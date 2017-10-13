from model_mommy import mommy
from django.shortcuts import resolve_url
from githubstars.core.tests.mixins import BaseTest


class SearchTest(BaseTest):

    def setUp(self):
        self.login()

        self.obj1 = mommy.make('core.Repository', user=self.user, name='Java', url='http://github.com',
                               language='java')
        self.obj2 = mommy.make('core.Repository', user=self.user, name='Python', url='http://github.com',
                               language='python')
        self.obj3 = mommy.make('core.Repository', user=self.user, name='Javascript', url='http://github.com',
                               language='javascript')

        self.obj1.tags.add(mommy.make('core.Tag', name='java'))
        self.obj2.tags.add(mommy.make('core.Tag', name='python'))
        self.obj3.tags.add(mommy.make('core.Tag', name='javascript'))

    def test_filter_by_tag_java(self):
        response = self.client.get('{}?tag_name=java'.format(resolve_url('repositories')),
                                   HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEqual(2, len(response.json()))

    def test_filter_by_tag_python(self):
        response = self.client.get('{}?tag_name=python'.format(resolve_url('repositories')),
                                   HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEqual(1, len(response.json()))

    def test_filter_by_tag_not_exists(self):
        response = self.client.get('{}?tag_name=not_exists'.format(resolve_url('repositories')),
                                   HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEqual(0, len(response.json()))

