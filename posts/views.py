from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator


def posts_list(request):
    posts = Post.objects.filter(published=True)
    q = request.GET.get('q')

    if q:
        posts = posts.filter(title__icontains=q)

    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    posts_lis = paginator.get_page(page_number)
    return render(request, 'posts/list.html', {'posts_lis': posts_lis})


def post_details(request, pk):
    post = Post.objects.get(pk=pk)
    context = {}
    if post.published:
        context['post'] = post
    return render(request, 'posts/details.html', context)


def add_post_form(request):
    if request.method == 'POST' and request.user.is_authenticated:
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            form.save_m2m()

            return HttpResponseRedirect(reverse('posts:add'))
    else:
        form = PostForm()

    return render(request, 'posts/add.html', {'form': form})


def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST' and request.user.is_authenticated:
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            form.save_m2m()
    else:
        form = PostForm(instance=post)

    return render(request, 'posts/add.html', {'form': form})
