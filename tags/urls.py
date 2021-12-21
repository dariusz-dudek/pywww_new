from django.urls import path
from tags.views import TagAutocomplete


app_name = 'tags'
urlpatterns = [
    path('tag-autocomplete/$', TagAutocomplete.as_view(), name='tag-autocomplete'),
]
