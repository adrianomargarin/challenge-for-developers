from django.contrib import admin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from githubstars.core.models import Repository


@admin.register(Repository)
class RepositoryAdmin(admin.ModelAdmin):

    list_display = ['user', 'name', 'url_github', 'tags', 'created_at', 'updated_at']
    list_display_links = ['user', 'name']
    readonly_fields = ['repo_id', 'name', 'url', 'user', 'language', 'created_at', 'updated_at']

    def url_github(self, obj):
        return '<a href="{0}" target="_blank">{0}</a>'.format(obj.url)

    url_github.allow_tags = True
    url_github.short_description = 'URL Github'

    def get_queryset(self, request):
        queryset = super(RepositoryAdmin, self).get_queryset(request)

        if request.user.is_superuser:
            return queryset

        return queryset.filter(user=request.user)

    def response_change(self, request, obj):
        if '_continue' not in request.POST:
            return HttpResponseRedirect(reverse_lazy('home'))
        else:
            return super(RepositoryAdmin, self).response_change(request, obj)
