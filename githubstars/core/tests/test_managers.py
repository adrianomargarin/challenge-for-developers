from model_mommy import mommy
from githubstars.core.models import Repository
from githubstars.core.tests.mixins import BaseTest


class RepositoryManagerTest(BaseTest):

    def setUp(self):
        self.create_user()
        self.obj1 = mommy.make('core.Repository', user=self.user)
        self.obj2 = mommy.make('core.Repository', user=self.user)
        self.obj3 = mommy.make('core.Repository', user=self.user)
        self.obj4 = mommy.make('core.Repository')

        self.obj1.tags.add(mommy.make('core.Tag', name='java'))
        self.obj2.tags.add(mommy.make('core.Tag', name='python'))
        self.obj3.tags.add(mommy.make('core.Tag', name='javascript'))

    def test_filter_by_tag_java(self):
        self.assertEqual(2, Repository.objects.filter_by_tag(self.user, 'java').count())

    def test_filter_by_tag_python(self):
        self.assertEqual(1, Repository.objects.filter_by_tag(self.user, 'python').count())

    def test_filter_by_tag_not_exists(self):
        self.assertEqual(0, Repository.objects.filter_by_tag(self.user, 'not_exists').count())

    def test_filter_by_user(self):
        self.assertEqual(3, Repository.objects.filter_by_user(self.user).count())
