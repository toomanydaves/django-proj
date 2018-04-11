from .models import Post
from django.shortcuts import render

def blog(request):
    posts_list = Post.objects.all()
    return render(request, 'blog/blog.html', { 'posts_list': posts_list })
