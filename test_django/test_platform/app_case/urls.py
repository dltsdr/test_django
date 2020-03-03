from django.urls import path
from app_case import views

urlpatterns = [
    #用例管理
    path('', views.list_case),
    path('send_req/', views.send_req),

]
