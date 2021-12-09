from django.urls import path
from .views import index, about

app_name = 'main'

urlpatterns = [
    path('', index, name='hello_world'),
    path('about/', about, name='about')
]
