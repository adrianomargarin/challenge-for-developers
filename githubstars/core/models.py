from django.db import models


class Tag(models.Model):

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    name = models.CharField(verbose_name='Nome', max_length=255, unique=True)
    created_at = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)

    def __str__(self):
        return self.name


class Repository(models.Model):

    class Meta:
        verbose_name = 'Repositório'
        verbose_name_plural = 'Repositórios'

    repo_id = models.PositiveIntegerField(verbose_name='ID do Repositório')
    name = models.CharField(verbose_name='Nome', max_length=255)
    url = models.URLField(verbose_name='URL do Repositório')
    username = models.CharField(verbose_name='Usuário', max_length=255)
    language = models.CharField(verbose_name='Linguagem', max_length=255)
    tags = models.ManyToManyField(Tag, verbose_name='Tags')
    created_at = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)

    def __str__(self):
        return self.name
