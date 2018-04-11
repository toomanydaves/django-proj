import random

from .models import Peep
from blog.models import Post
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

def index(request):
    return render(request, 'network/network.html')

def peep(request, peep_id):
    peep = get_object_or_404(Peep, pk=peep_id)
    return render(request, 'network/peep.html', { 'peep': peep })

def peeps(request):
    peeps_list = Peep.objects.all()
    return render(request, 'network/peeps.html', { 'peeps_list': peeps_list })

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
            written_by=request.user.peep,
            status='DRAFT',
        ).order_by(
            '-published_at'
        ),
        'published_list': Post.objects.filter(
            written_by=request.user.peep,
            status='PUBLISHED'
        ).order_by(
            '-created_at'
        ),
    })
