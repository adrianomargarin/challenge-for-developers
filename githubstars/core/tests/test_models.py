from datetime import datetime
from django.core.exceptions import ValidationError

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

    def test_create_with_duplicate_tag(self):
        with self.assertRaises(ValidationError):
            obj = Repository(user=self.user, repo_id=1, name='Test 2', url='http://github.com', tags='python, python')
            obj.clean_fields()

