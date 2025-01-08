"""Blog Views"""

from django.shortcuts import get_object_or_404, render
from .models import Post


def post_list(request):
    """List all posts"""
    posts = Post.published.all()
    return render(request, "blog/post/list.html", {"posts": posts})


def post_detail(request, post_id):
    """List post detail"""
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    return render(request, "blog/post/detail.html", {"post": post})
