from django.shortcuts import render

def project(request, project_id):
    #Get the project by id
    return render(request, 'portfolio/project.html')

def projects(request):
    return render(request, 'portfolio/projects.html')
