from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from app_manage.models import Project
from app_manage.forms import ProjectForm


@login_required
def manage(request):
    #项目管理
    projects_list = Project.objects.all()
    return render(request, "project_list.html", {"projects":projects_list})

def add_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            status = form.cleaned_data['status']
            Project.objects.create(name=name, describe=describe, status=status)
        return HttpResponseRedirect("/project/")
    else:
        form = ProjectForm()
    return render(request, 'project_add.html', {'form': form})
