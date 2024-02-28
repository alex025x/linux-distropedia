from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "distroblog/index.html"
    paginate_by = 4

def post_detail(request, slug):
    post = get_object_or_404(Post.objects.filter(status=1, slug=slug))
    comments = post.comments.all().order_by("-created_at")
    comment_count = post.comments.filter(approved=True).count()
    return render(
        request, "distroblog/post_detail.html", 
        {
            "post": post,
            "comments": comments, 
            "comment_count": comment_count,
            },
    )
