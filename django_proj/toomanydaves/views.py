from django.contrib.auth import logout
from django.shortcuts import render
from portfolio.models import Project

def home(request):
    project_list = Project.objects.order_by('?')[:4]
    seen_home = True

    print(project_list)

    if request.session.get('seen_home', False):
        request.session['seen_home'] = True
        seen_home = False

    return render(request, 'toomanydaves/home.html', {
        'seen_home': seen_home,
        'project_list': project_list,
    })

def backstory(request):
    return render(request, 'toomanydaves/backstory.html')

def poem(request):
    return render(request, 'toomanydaves/poem.html')

def logout_user(request):
    logout(request)

    #Redirect to a success page
    return render(request, 'toomanydaves/home.html')

def engage(request):
    # TODO Like login
    # Render form / accept post / redirect to index

    return render(request, 'toomanydaves/engage.html')
