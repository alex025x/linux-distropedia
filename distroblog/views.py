from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "distroblog/index.html"
    paginate_by = 4

def post_detail(request, slug):
    post = get_object_or_404(Post.objects.filter(status=1, slug=slug))
    return render(request, "distroblog/post_detail.html", {"post": post})
