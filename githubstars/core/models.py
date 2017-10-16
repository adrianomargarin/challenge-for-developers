from django.db import models
from django.conf import settings
from githubstars.core.managers import RepositoryManager

from django.core.exceptions import ValidationError

def validate_tags(value):
    from IPython import embed; embed()


class Repository(models.Model):

    class Meta:
        verbose_name = 'Repositório'
        verbose_name_plural = 'Repositórios'
        ordering = ['name']

    repo_id = models.PositiveIntegerField(verbose_name='ID do Repositório')
    name = models.CharField(verbose_name='Nome', max_length=255)
    url = models.URLField(verbose_name='URL')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    language = models.CharField(verbose_name='Linguagem', max_length=255, null=True, blank=True)
    tags = models.CharField(verbose_name='Tags', max_length=255, null=True, blank=True)#, validators=[validate_tags])
    created_at = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)

    objects = RepositoryManager()

    def __str__(self):
        return self.name
