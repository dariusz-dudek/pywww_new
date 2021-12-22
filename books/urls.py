from django.urls import path
from .views import books_list, book_details, add_book_form, edit_book, AuthorAutocomplete

app_name = 'books'

urlpatterns = [
    path('<int:pk>', book_details, name='details'),
    path('', books_list, name='list'),
    path('add/', add_book_form, name='add'),
    path('<int:book_id>/edit', edit_book, name='edit'),
    path('author-autocomplete/', AuthorAutocomplete.as_view(), name='author-autocomplete'),
]