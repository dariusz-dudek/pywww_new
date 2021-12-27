from django.contrib.auth.models import Permission, User
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import RegisterForm


def register(response):
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            user = form.save()
            permission = Permission.objects.get(name='Can add tag')
            user.user_permissions.add(permission)
        return redirect(reverse('main:index'))
    else:
        form = RegisterForm()
    return render(response, 'accounts/register.html', {'form': form})