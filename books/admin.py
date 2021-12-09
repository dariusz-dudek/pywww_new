from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'publication_year']
    search_fields = ['title', 'description', 'author']
    list_filter = ['available']
