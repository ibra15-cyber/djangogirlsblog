# from datetime import timezone
from django.urls import is_valid_path
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Post #we import our Post to be able to talk with the db

# Create your views here.
def post_list(request):  #take a request as para
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # = get_object_or_404(Post, id)
    context = {
        'posts': posts
    }
    return render(request, 'blog/post_list.html', context) #return render pass the request and render .html

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# def post_new(request):
#     form = PostForm()
#     return render(request, 'blog/post_edit.html', {'form': form})

# what is happening here is that when a user goes to a link its get request
# so the html with the context is rendeered
# when the user submits, it a post request hence we get the user that posted it and teh time
# we setting the post.author to ther user making the request
# and also setting the post.published_date to when we did the submission whihc is now
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            form.save()
            return redirect('post_detail', id=post.id) #after submitting to the db, get us to the post_detail of the same post
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})



def post_edit(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})