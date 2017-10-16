from model_mommy import mommy
from githubstars.core.models import Repository
from githubstars.core.tests.mixins import BaseTest


class RepositoryManagerTest(BaseTest):

    def setUp(self):
        self.create_user()

        mommy.make('core.Repository', user=self.user, _quantity=5)

        self.obj1 = mommy.make('core.Repository', user=self.user, tags='java')
        self.obj2 = mommy.make('core.Repository', user=self.user, tags='python')
        self.obj3 = mommy.make('core.Repository', user=self.user, tags='javascript')

    def test_filter_by_tag_is_blank(self):
        self.assertEqual(8, Repository.objects.filter_by_tag(self.user, '').count())

    def test_filter_by_tag_java(self):
        self.assertEqual(2, Repository.objects.filter_by_tag(self.user, 'java').count())

    def test_filter_by_tag_python(self):
        self.assertEqual(1, Repository.objects.filter_by_tag(self.user, 'python').count())

    def test_filter_by_tag_not_exists(self):
        self.assertEqual(0, Repository.objects.filter_by_tag(self.user, 'not_exists').count())
