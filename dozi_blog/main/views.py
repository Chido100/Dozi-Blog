from django.shortcuts import render, get_object_or_404
from .models import Post



# Display all posts
def post_list(request):
    posts = Post.published.all()
    return render(request, 'main/post/list.html', {'posts': posts})



# Display single post
def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    return render(request, 'main/post/detail.html', {'post': post})
