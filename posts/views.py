from django.shortcuts import render
from .models import Post


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/list.html', {'posts': posts})


def post_details(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'posts/details.html', {'post': post})
