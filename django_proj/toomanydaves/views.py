from django.contrib.auth import logout
from django.shortcuts import render

def index(request):
    return render(request, 'toomanydaves/index.html')

def about(request):
    return render(request, 'toomanydaves/about.html')

def logout_user(request):
    logout(request)

    #Redirect to a success page
    return render(request, 'toomanydaves/index.html')

def engage(request):
    # TODO Like login
    # Render form / accept post / redirect to index

    return render(request, 'toomanydaves/engage.html')
