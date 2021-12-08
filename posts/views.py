from django.shortcuts import render
from .models import Post


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/posts_list.html', {'posts': posts})


def post_details(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'posts/post_details.html', {'post': post})
