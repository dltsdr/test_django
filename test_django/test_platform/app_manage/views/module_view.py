from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from app_manage.models import Project
from app_manage.forms import ProjectForm,ProjectEditForm
from app_manage.models import Module

def list_module(request):
    """
    模块管理
    """
    module_list = Module.objects.all()
    return render(request, "module/list.html", {
        "modules":module_list})
