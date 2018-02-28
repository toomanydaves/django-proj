from blog.models import Post
from django.contrib.auth import logout
from django.shortcuts import render
from portfolio.models import Project
from network.models import Peep

def home(request):
    return_visit = True

    if request.session.get('return_visit', False):
        return_visit = False
        request.session['return_visit'] = True

    return render(request, 'toomanydaves/home.html', {
        'return_visit': return_visit,
        'project_list': Project.objects.order_by('?')[:8],
        'post_list': Post.objects.filter(status='PUBLISHED').order_by('-published_at')[:4],
        'peeps_list': Peep.objects.order_by('?')[:8],
    })

def backstory(request):
    return render(request, 'toomanydaves/backstory.html')

def poem(request):
    return render(request, 'toomanydaves/poem.html')

def logout_user(request):
    logout(request)

    # TODO Redirect to home page
    return render(request, 'toomanydaves/home.html')

def engage(request):
    # TODO Like login
    # Render form / accept post / redirect to index

    return render(request, 'toomanydaves/engage.html')
