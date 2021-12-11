from django.urls import path
from .views import books_list, book_details

app_name = 'books'

urlpatterns = [
    path('<int:pk>', book_details, name='details'),
    path('', books_list, name='list'),


]