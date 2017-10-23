from django.shortcuts import render, get_object_or_404
from .models import Project, Tag

def home(request):
    project_list = Project.objects.all()
    tag_list = Tag.objects.all()
    return render(request, 'portfolio/projects.html', {
        'project_list': project_list,
        'tag_list': tag_list,
    })

def project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'portfolio/project.html', {'project': project})
