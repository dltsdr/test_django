from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app_manage.models import Project
# Create your views here.
@login_required
def manage(request):
    #接口管理
    projects_list = Project.objects.all()
    return render(request, "manage.html", {"projects":projects_list})