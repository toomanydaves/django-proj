import random

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def index(request):
    return render(request, 'network/network.html')

@login_required
def dashboard(request):
    greetings = [
        'Hola',
        'Yo',
        'Wilkommen',
        'Bienvenue',
        'As-salāmu ʿalaykum',
        'Shalom aleikhem',
        
    ]
    return render(request, 'network/dashboard.html', {
        'greeting': random.choice(greetings)
    })
