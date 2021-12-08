from django.urls import path
from .views import hello_world, about

urlpatterns = [
    path('', hello_world),
    path('about/', about)
]
