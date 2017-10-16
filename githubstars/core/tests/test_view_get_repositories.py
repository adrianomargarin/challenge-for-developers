from django.shortcuts import resolve_url
from githubstars.core.models import Repository
from githubstars.core.tests.mixins import BaseTest


class GetRepositories(BaseTest):

    def setUp(self):
        self.login()
        self.response = self.client.get(resolve_url('get_repositories'))

    # def test_get_repositories(self):
    #     self.assertEqual(302, self.response.status_code)

    # def test_repositories_exists(self):
    #     self.assertTrue(Repository.objects.exists())
