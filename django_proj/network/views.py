import random

from blog.models import Post
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def index(request):
    return render(request, 'network/network.html')

@login_required
def dashboard(request):
    greetings = [
        'Hola',
        'Holla',
        'Yo',
        'Willkommen',
        'Bienvenue',
        'As-salāmu ʿalaykum',
        'Shalom aleikhem',
        
    ]
    return render(request, 'network/dashboard.html', {
        'greeting': random.choice(greetings),
        'draft_list': Post.objects.filter(
            written_by=request.user,
            status='DRAFT',
        ).order_by(
            '-published_at'
        ),
        'published_list': Post.objects.filter(
            written_by=request.user,
            status='PUBLISHED'
        ).order_by(
            '-created_at'
        ),
    })
