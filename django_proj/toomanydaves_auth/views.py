from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import User

def person(request, user_id):
    person = get_object_or_404(User, pk=user_id)
    return render(request, 'toomanydaves_auth/person.html', {'person': person})

def people(request):
    people_list = User.objects.all()
    return render(request, 'toomanydaves_auth/people.html', {'people_list': people_list})
