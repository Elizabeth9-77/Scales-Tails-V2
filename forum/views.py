from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from django.utils import timezone
from .models import Post, Comment, Reply
from .forms import CommentForm, ReplyForm

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "forum/index.html"
    paginate_by = 6

def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        # handle comment form
        if "comment_form" in request.POST:
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.post = post
                comment.save()
                messages.success(request,'Comment submitted and awaiting approval')
                return redirect('post_detail', slug=post.slug)
            else:
                messages.error(request, 'There was an error submitting your comment, please try again')
    #     else:
    #         comment_form = CommentForm

    # comment_form = CommentForm()

        # handle the reply form
        elif "reply_form" in request.POST:
            reply_form =  ReplyForm(data=request.POST)
            if reply_form.is_valid():
                reply = reply_form.save(commit=False)
                reply.user = request.user
                reply.timestamp = timezone.now()

                comment_id = request.POST.get("comment_id")
                try:
                    comment = Comment.objects.get(id=comment_id)
                    reply.comment = comment
        
                    # handle nested replies
                    parent_id = request.POST.get("parent_id")
                    if parent_id:
                        parent_reply = get_object_or_404(Reply, id=parent_id)
                        reply.parent = parent_reply

                    reply.save()
                    messages.success(request, 'Reply submitted.')
                except Comment.DoesNotExist:
                    messages.error(request, 'There was an error submiting your reply, please try again')
                return redirect('post_detail', slug=post.slug)
            else:
                messages.error(request, 'There was an error submitting your comment, please try again')
    else:
        comment_form = CommentForm()
        reply_form = ReplyForm()

    return render(
        request,
        "forum/post_detail.html",
        {
            "post" : post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            "reply_form": reply_form
        }
    )