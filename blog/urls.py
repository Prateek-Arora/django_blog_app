from django.urls import path
from blog.views import post_list, post_detail, post_new, post_edit, post_delete, post_draft_list, post_publish, comment_remove, comment_approve, signup, user_profile

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<int:pk>', post_detail, name='post_detail'),
    path('post/new', post_new, name='post_new'),
    path('post/<int:pk>/edit', post_edit, name='post_edit'),
    path('post/<int:pk>/delete', post_delete, name='post_delete'),
    path('drafts/', post_draft_list, name='post_draft_list'),
    path('post/<int:pk>/publish/', post_publish, name='post_publish'),


    path('comment/<int:pk>/remove/', comment_remove, name='comment_remove'),
    path('comment/<int:pk>/approve/', comment_approve, name='comment_approve'),

    path('signup/', signup, name='signup'),

    path('user/<int:pk>', user_profile, name='user_profile'),

]


