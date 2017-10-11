from datetime import datetime
from django.test import TestCase

from githubstars.core.models import Tag
from githubstars.core.models import Repository


class RepositoryModelTest(TestCase):

    def setUp(self):
        self.obj = Repository(repo_id=1, name='Test', url='http://github.com', language='python')
        self.obj.save()

    def test_create(self):
        self.assertTrue(Repository.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Test', str(self.obj))


class TagModelTest(TestCase):

    def setUp(self):
        self.obj = Tag(name='python')
        self.obj.save()

    def test_create(self):
        self.assertTrue(Tag.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('python', str(self.obj))
