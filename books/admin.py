from django.contrib import admin
from .models import Book, Author
from import_export import resources
from import_export.admin import ExportMixin


class BookResource(resources.ModelResource):
    class Meta:
        model = Book


class AuthorResource(resources.ModelResource):
    class Meta:
        model = Author


@admin.register(Book)
class BookAdmin(ExportMixin, admin.ModelAdmin):
    exclude = ['authors']
    list_display = ['id', 'title', 'available']
    search_fields = ['title', 'description', 'authors__name']
    list_filter = ['available']
    autocomplete_fields = ['tags']
    resource_class = BookResource


@admin.register(Author)
class AuthorAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['id', 'name', 'birth_year']
    search_fields = ['name']
    resource_class = AuthorResource
