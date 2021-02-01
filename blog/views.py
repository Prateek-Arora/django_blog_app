from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from blog.forms import PostForm, CommentForm, UserForm
from .models import Post, Comment

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    stuff_for_frontend = {'posts': posts}
    return render(request, 'blog/post_list.html', stuff_for_frontend)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.post = post
                comment.save()
                return redirect('post_detail', pk=post.pk)
        else:
            return redirect('login')
    else:
        form = CommentForm()
    stuff_for_frontend = {'post': post, 'form': form,'user': user}
    return render(request, 'blog/post_detail.html', stuff_for_frontend)


@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        stuff_for_frontend = {'form': form}
    return render(request, 'blog/post_edit.html', stuff_for_frontend)


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST' and (request.user == post.author or request.user.is_superuser):

        #updating an existing form.
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    elif request.method != 'POST' and (request.user == post.author or request.user.is_superuser):
        form = PostForm(instance=post)
        stuff_for_frontend = {'form': form}
        return render(request, 'blog/post_edit.html', stuff_for_frontend)
    return redirect('post_detail', pk=post.pk)


@login_required
def post_draft_list(request, pk):
    user = get_object_or_404(User, pk=pk)
    posts = Post.objects.filter(author=user).filter(published_date__isnull=True).order_by('-created_date')
    stuff_for_frontend = {'posts': posts}
    return render(request, 'blog/post_draft_list.html', stuff_for_frontend)


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')



# def add_comment_to_post(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.author = request.user
#             comment.post = post
#             comment.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = CommentForm()
#     return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('/')
    else:
        form = UserForm()
    return render(request, 'blog/signup.html', {'form': form})


@login_required
def user_profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    user_posts = Post.objects.filter(author=user).filter(published_date__isnull=False).count
    user_drafts = Post.objects.filter(author=user).filter(published_date__isnull=True).count
    user_comments = Comment.objects.filter(author=user).count
    stuff_for_frontend = {'user': user, 'user_posts': user_posts, 'user_comments': user_comments,'user_drafts': user_drafts}
    return render(request, 'blog/user_profile.html', stuff_for_frontend)


@login_required
def user_posts(request, pk):
    user = get_object_or_404(User, pk=pk)
    user_posts = Post.objects.filter(author=user).filter(published_date__isnull=False).order_by('-created_date')
    stuff_for_frontend = {'user': user, 'user_posts': user_posts}
    return render(request, 'blog/user_posts.html', stuff_for_frontend)

