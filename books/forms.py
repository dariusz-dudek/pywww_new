from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        # fields = ['title', 'description', 'available', 'publication_year', 'authors', 'tags', 'cover']
        fields = '__all__'
        labels = {
            'title': 'Tytuł',
            'description': 'Opis',
            'available': 'Dostępność',
            'publication_year': 'Rok wydania',
            'authors': 'Autorzy',
            'tags': 'Tagi',
            'cover': 'Okładka'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'books:add'
        self.helper.layout = Layout(
            Fieldset(
                'Dodawanie książki',
                'title',
                'authors',
                'description',
                'publication_year',
                'available',
                'tags',
                'cover'
            ),
            ButtonHolder(
                Submit('submit', 'Dodaj', css_class='btn btn-primary'),
                css_class='d-flex justify-content-end'
            )
        )


class BookBorrowForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('borrow', 'Wypożycz'))

