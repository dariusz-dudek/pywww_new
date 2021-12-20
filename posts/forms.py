from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, HTML, ButtonHolder
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content', 'sponsored', 'published', 'image', 'tags']
        labels = {
            'title': 'Tytuł',
            'content': 'Treść',
            'sponsored': 'Sponsorowany',
            'published': 'Opublikowany',
            'image': 'Obraz',
            'tags': 'Tagi'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = '?'
        self.helper.layout = Layout(
            Fieldset(
                'Dodawanie postu',
                'title',
                'content',
                'sponsored',
                'published',
                'image',
                'tags'
            ),
            ButtonHolder(
                Submit('submit', 'Dodaj', css_class='btn btn-primary'),
                css_class='d-flex justify-content-end'
            )
        )
