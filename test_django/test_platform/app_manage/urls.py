from django.urls import path
from app_manage.views import project_view
from app_manage.views import module_view

urlpatterns = [
    #项目管理 test_platform.urls会调用这里的
    path('1/', project_view.list_project),
    path('add', project_view.add_project),
    path('edit/<int:pid>/', project_view.edit_project),
    path('delete/<int:pid>/', project_view.delete_project),

    #模块管理
    path('2/', module_view.list_module),

]
