from django.urls import path
from .views import books_list, book_details, add_book_form, edit_book, handle_book_borrows

app_name = 'books'

urlpatterns = [
    path('<int:pk>', book_details, name='details'),
    path('', books_list, name='list'),
    path('add/', add_book_form, name='add'),
    path('<int:book_id>/edit', edit_book, name='edit'),
    path('<int:book_id>/borrows', handle_book_borrows, name='borrows')
]