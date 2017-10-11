from django.contrib import admin

from githubstars.core.models import Repository


@admin.register(Repository)
class RepositoryAdmin(admin.ModelAdmin):

    list_display = ['username', 'name', 'url', 'created_at']
    search_fields = ['username']
    list_filter = ['username']
