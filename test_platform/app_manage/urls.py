from django.urls import path
from app_manage import views


urlpatterns = [
    #项目管理
    path('', views.manage),
    path('add', views.add_project),
]