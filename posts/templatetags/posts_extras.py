from django import template

register = template.Library()


@register.simple_tag
def count_sings(text):
    return len(text)


@register.simple_tag
def count_words(text):
    return len(text.split())
