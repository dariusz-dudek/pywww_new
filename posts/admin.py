from django.contrib import admin
from .models import Post
from import_export import resources
from import_export.admin import ExportMixin


class PostResource(resources.ModelResource):
    class Meta:
        model = Post


@admin.register(Post)
class PostAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['id', 'title', 'created', 'modified', 'published', 'sponsored']
    search_fields = ['title', 'description']
    list_filter = ['published', 'sponsored']
    # filter_horizontal = ['tags']
    autocomplete_fields = ('tags',)
    resource_class = PostResource

