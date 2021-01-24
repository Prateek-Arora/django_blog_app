from django.urls import path
from blog.views import post_list, post_detail, post_new, post_edit, post_draft_list, post_publish

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<int:pk>', post_detail, name='post_detail'),
    path('post/new', post_new, name='post_new'),
    path('post/<int:pk>/edit', post_edit, name='post_edit'),
    path('drafts/', post_draft_list, name='post_draft_list'),
    path('post/<int:pk>/publish/', post_publish, name='post_publish'),

]


