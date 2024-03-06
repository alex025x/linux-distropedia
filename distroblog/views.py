from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from .models import Post, Comment, LikePost
from .forms import CommentForm, CreateBlogForm
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.http import HttpResponse
from django.http import HttpResponseRedirect



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

def comment_edit(request, slug, comment_id):
    """
    Edit comments view
    """
    if request.method == "POST":
        post = Post.objects.filter(status=1).get(slug=slug)
        comment = Comment.objects.get(pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.success(request, 'Comment updated successfully!')
        else:
            messages.error(request, 'Failed to update comment.')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

@login_required
def create_blog(request):
    if request.method == 'POST':
        form = CreateBlogForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            
            # Generate the slug
            if not new_post.slug:
                title = form.cleaned_data['title']  # Retrieve title from form
                slug = form.generate_unique_slug(title)  # Generate unique slug
                new_post.slug = slug

            try:
                new_post.save()
                messages.success(request, 'Blog post created successfully.')
                return redirect('home')
            except Exception as e:
                messages.error(request, f'An error occurred while saving the blog post: {str(e)}')
    else:
        form = CreateBlogForm()
    return render(request, 'distroblog/create_blog.html', {'form': form})

@login_required(login_url='signin')
def like_post(request):
    if request.method == 'GET':
        post_id = request.GET.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        username = request.user.username

        like_filter = LikePost.objects.filter(post_id=post_id, username=username).first()

        if like_filter is None:
            new_like = LikePost.objects.create(post_id=post_id, username=username)
            post.no_of_likes += 1
            post.save()
        else:
            like_filter.delete()
            post.no_of_likes -= 1
            post.save()

    return redirect(request.META.get('HTTP_REFERER', 'home'))