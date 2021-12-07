from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def posts_list(request):
    return HttpResponse(Post.objects.all())


def post_details(request, pk):
    post = Post.objects.get(pk=pk)
    return HttpResponse(
        f'''<h2>{post.title}</h2>
        <div>
            <small>Utworzono {post.created}, zmodyfikowano {post.modified}</small>
        </div>
        <div>
            <p>{post.content}</p>
        </div>'''
    )
