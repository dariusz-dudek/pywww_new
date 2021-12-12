from django.shortcuts import render
from .models import Post


def posts_list(request):
    posts = Post.objects.filter(published=True)
    return render(request, 'posts/list.html', {'posts': posts})


def post_details(request, pk):
    post = Post.objects.get(pk=pk)
    context = {}
    if post.published:
        context['post'] = post
    return render(request, 'posts/details.html', context)
