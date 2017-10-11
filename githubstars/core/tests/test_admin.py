from django.test import TestCase

from githubstars.core.admin import admin
from githubstars.core.admin import Tag
from githubstars.core.admin import Repository
from githubstars.core.admin import RepositoryAdmin


class RepositoryAdminTest(TestCase):

    def setUp(self):
        self.tag1 = Tag.objects.create(name='python')
        self.tag2 = Tag.objects.create(name='django')
        self.repository = Repository.objects.create(repo_id=1, name='Test', url='http://github.com', language='python')
        self.repository.tags.add(self.tag1)
        self.repository.tags.add(self.tag2)
        self.model_admin = RepositoryAdmin(Repository, admin.site)

    def test_url_github(self):
        expected = '<a href="http://github.com" target="_blank">http://github.com</a>'

        self.assertEqual(expected, self.model_admin.url_github(self.repository))

    def test_tags(self):
        result = ['python', 'django']

        self.assertSequenceEqual(result, self.model_admin._tags(self.repository))
