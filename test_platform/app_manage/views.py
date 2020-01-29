from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app_manage.models import Project
# Create your views here.


@login_required
def manage(request):
    #项目管理
    projects_list = Project.objects.all()
    return render(request, "project_list.html", {"projects":projects_list})

def add_project(request):
    print("chuangjianxiangmu")
    return render(request, "project_add.html", )
