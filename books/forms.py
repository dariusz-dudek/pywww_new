from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder
from dal import autocomplete
from tags.models import Tag
from .models import Book, Author
from dal import autocomplete


class BookForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='tags:tag-autocomplete')
    )
    authors = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='books:author-autocomplete')
    )

    class Meta:
        model = Book
        # fields = ['title', 'description', 'available', 'publication_year', 'authors', 'tags', 'cover']
        fields = "__all__"
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
        # self.helper.form_action = '?'
        self.helper.form_action = '?'
        self.helper.add_input(Submit('submit', 'Wyślij'))
        # self.helper.layout = Layout(
        #     Fieldset(
        #         'Dodawanie książki',
        #         'title',
        #         'authors',
        #         'description',
        #         'publication_year',
        #         'available',
        #         'tags',
        #         'cover'
        #     ),
        #     ButtonHolder(
        #         Submit('submit', 'Dodaj', css_class='btn btn-primary'),
        #         css_class='d-flex justify-content-end'
        #     )
        # )
