from datetime import datetime

from githubstars.core.models import Tag
from githubstars.core.models import Repository
from githubstars.core.tests.mixins import BaseTest


class RepositoryModelTest(BaseTest):

    def setUp(self):
        self.create_user()
        self.obj = Repository(user=self.user, repo_id=1, name='Test', url='http://github.com', language='python')
        self.obj.save()

    def test_create(self):
        self.assertTrue(Repository.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Test', str(self.obj))


class TagModelTest(BaseTest):

    def setUp(self):
        self.obj = Tag(name='python')
        self.obj.save()

    def test_create(self):
        self.assertTrue(Tag.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('python', str(self.obj))
