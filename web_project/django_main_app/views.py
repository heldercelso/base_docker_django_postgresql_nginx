from django.shortcuts import render
#from projects.models import Project

def project_index(request):
    #projects = Project.objects.all()
    #context = {
    #    'projects': projects
    #}
    context = {}
    return render(request, 'project_index.html', context)