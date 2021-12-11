from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


def books_list(request):
    books = Book.objects.all()
    return render(request, 'books/books_list.html', {'books': books})


def book_details(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'books/book_details.html', {'book': book})
