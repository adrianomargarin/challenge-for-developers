from django.test import TestCase

from githubstars.core.githubapi import GithubAPI


class GithubAPITestCase(TestCase):

    def test_get_repositories(self):
        response = GithubAPI('adrianomargarin').get_repositories()

        self.assertEqual(response.status_code, 200)

    def test_get_content(self):
        content = GithubAPI('adrianomargarin').get_content()

        self.assertEqual(len(content), 30)
