from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Post
from .forms import CommentForm

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "distroblog/index.html"
    paginate_by = 6

def post_detail(request, slug):
    post = get_object_or_404(Post.objects.filter(status=1, slug=slug))
    comments = post.comments.all().order_by("-created_at")
    comment_count = post.comments.filter(approved=True).count()
    comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                    request, messages.SUCCESS,
                    'Comment submitted and awaiting approval'
    )

    return render(
        request, "distroblog/post_detail.html", 
        {
            "post": post,
            "comments": comments, 
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )
