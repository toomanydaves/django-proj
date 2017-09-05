from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def user(request):
    return render(request, 'toomanydaves_auth/user.html')
