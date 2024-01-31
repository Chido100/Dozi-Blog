from django.shortcuts import render, get_object_or_404
from .models import Post



# Display all posts
def post_list(request):
    posts = Post.published.all()
    return render(request, 'main/post/list.html', {'posts': posts})



# Display single post
def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day
    )
    return render(request, 'main/post/detail.html', {'post': post})
