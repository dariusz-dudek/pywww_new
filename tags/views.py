from django.shortcuts import render
from dal import autocomplete
from tags.models import Tag


class TagAutocomplete(autocomplete.Select2QuerySetSequenceView):
    def get_queryset(self):
        if not self.request.user.is_autenticated:
            return Tag.objects.none()

        qs = Tag.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs
