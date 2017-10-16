from django.db import models


class RepositoryManager(models.Manager):

    def filter_by_tag(self, user, tag_name):
        if tag_name:
            return self.filter(user=user, tags__icontains=tag_name)

        return self.filter(user=user)
