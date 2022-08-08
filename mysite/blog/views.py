# from datetime import timezone
from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from .models import Post #we import our Post to be able to talk with the db

# Create your views here.
def post_list(request):  #take a request as para
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts}) #return render pass the request and render .html

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})