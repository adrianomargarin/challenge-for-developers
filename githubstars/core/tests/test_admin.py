from githubstars.core.admin import admin
from githubstars.core.admin import Tag
from githubstars.core.admin import Repository
from githubstars.core.admin import RepositoryAdmin
from githubstars.core.tests.mixins import BaseTest


class RepositoryAdminTest(BaseTest):

    def setUp(self):
        self.create_user()
        self.tag1 = Tag.objects.create(name='python')
        self.tag2 = Tag.objects.create(name='django')
        self.repository = Repository.objects.create(user=self.user, repo_id=1, name='Test', url='http://github.com',
                                                    language='python')
        self.repository.tags.add(self.tag1)
        self.repository.tags.add(self.tag2)
        self.model_admin = RepositoryAdmin(Repository, admin.site)

    def test_url_github(self):
        expected = '<a href="http://github.com" target="_blank">http://github.com</a>'

        self.assertEqual(expected, self.model_admin.url_github(self.repository))

    def test_tags(self):
        self.assertSequenceEqual('python, django', self.model_admin._tags(self.repository))
