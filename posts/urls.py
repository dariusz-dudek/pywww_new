from django.urls import path
from .views import posts_list, post_details,  add_post_form, edit_post

app_name = 'posts'


urlpatterns = [
    path('<int:pk>/', post_details, name='details'),
    path('', posts_list, name='list'),
    path('add/', add_post_form, name='add'),
    path('<int:post_id>/edit', edit_post, name='edit')
]
