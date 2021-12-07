from django.urls import path
from .views import posts_list, post_details


urlpatterns = [
    path('<int:pk>/', post_details),
    path('', posts_list),
]
