from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from app_manage.models import Project
from app_manage.forms import ProjectForm,ProjectEditForm


@login_required
#项目管理
def manage(request):
    projects_list = Project.objects.all()
    return render(request, "project_list.html", {"projects":projects_list})

#创建项目
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

#编辑项目
def edit_project(request, pid):
    print(pid)
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            status = form.cleaned_data['status']

            p = Project.objects.get(id=pid)
            p.name = name
            p.describe = describe
            p.status = status
            p.save()

        return HttpResponseRedirect("/project/")
    else:
        if pid:
        #判断pid是否存在，如果存在则进行下面的逻辑
            p = Project.objects.get(id=pid)
            form = ProjectEditForm(instance=p)
        else:
            form = ProjectForm()
        return render(request,'project_edit.html', {
            'form': form, "id": pid})