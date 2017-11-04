from django.contrib.auth import logout
from django.shortcuts import render

def home(request):
    return render(request, 'toomanydaves/home.html')

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
