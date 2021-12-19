from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Book, Borrow
from .forms import BookForm, BookBorrowForm
from django.urls import reverse
from django.utils import timezone


def books_list(request):
    books = Book.objects.all()
    return render(request, 'books/books_list.html', {'books': books})


def book_details(request, pk):
    book = Book.objects.get(pk=pk)
    form = BookBorrowForm()
    form.helper.form_action = reverse('books:borrows', args=[pk])
    return render(request, 'books/book_details.html', {'book': book, 'form': form})


def add_book_form(request):
    if request.method == 'POST' and request.user.is_authenticated:
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('books:add'))
    else:
        form = BookForm()

    return render(request, 'books/add.html', {'form': form})


def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST' and request.user.is_authenticated:
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
    else:
        form = BookForm(instance=book)

    return render(request, 'books/add.html', {'form': form})


def handle_book_borrows(request, book_id=None):
    user = request.user
    if request.method == 'POST':
        if user.is_authenticated:
            if request.POST.get('borrow'):
                book = Book.objects.get(pk=book_id)
                Borrow.objects.create(
                    user=user,
                    book=book
                )
                book.available = False
                book.save()
                return HttpResponseRedirect(reverse('books:details', args=[book_id]))
            else:
                keys = [key for key in request.POST.keys() if key.startswith('book_')]
                key = int(keys[0].split('_')[1])
                book = Book.objects.get(pk=key)
                borrow = Borrow.objects.filter(user=user, book=book).last()
                if not borrow.return_date:
                    borrow.return_date = timezone.now()
                    borrow.save()
                    book.available = True
                    book.save()
                return HttpResponseRedirect(reverse('books:borrows_list'))
    else:
        borrows = Borrow.objects.filter(user=user)
        return render(request, 'books/borrows_list.html', {'borrows': borrows})

