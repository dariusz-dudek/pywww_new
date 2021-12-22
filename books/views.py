from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Book, Author
from .forms import BookForm
from django.urls import reverse
from dal import autocomplete


def books_list(request):
    books = Book.objects.all()
    return render(request, 'books/books_list.html', {'books': books})


def book_details(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'books/book_details.html', {'book': book})


def add_book_form(request):
    if request.method == 'POST' and request.user.is_authenticated:
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            form.save_m2m()

            return HttpResponseRedirect(reverse('books:add'))
    else:
        form = BookForm()

    return render(request, 'books/add.html', {'form': form})


def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST' and request.user.is_authenticated:
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            form.save_m2m()
    else:
        form = BookForm(instance=book)

    return render(request, 'books/add.html', {'form': form})


class AuthorAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Author.objects.none()

        qs = Author.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs

