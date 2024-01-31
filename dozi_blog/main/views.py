from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm
from django.core.mail import send_mail



# Display all posts
def post_list(request):
    post_list = Post.published.all()
    # Paginate with 3 posts per page
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

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




# Share post via email
def post_share(request, post_id):
    # Retrieve post by ID
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(
                post.get_absolute_url()
            )
            subject = f"{cd['name']} recommends you read {post.title}"
            message = f"Read {post.title} at {post_url} {cd['name']} comments: {cd['comments']}"
            send_mail(subject, message, 'chidozieamefule@googlemail.com', [cd['to']])
            sent = True
    
    else:
        form = EmailPostForm()
    return render(request, 'main/post/share.html', {'form': form, 'post': post, 'sent': sent})
    

