from .models import Project, Tag
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

def home(request):
    included_tags = [int(tag) for tag in request.GET.getlist('tag')]
    included_projects = []
    tag_list = Tag.objects.all()
    project_list = Project.objects.all()

    if included_tags:
        for tag in tag_list:
            if not tag.id in included_tags:
                tag.exclude = True

        for project in project_list:
            if not set(included_tags).intersection(project.tags.values_list('id', flat=True)):
                project.exclude = True
            else:
                included_projects.append(project.id)

    if not request.is_ajax():
        return render(request, 'portfolio/projects.html', {
            'tag_list': tag_list,
            'project_list': project_list,
        })
    else:
        return JsonResponse(included_projects, safe=False)

def project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'portfolio/project.html', {'project': project})
