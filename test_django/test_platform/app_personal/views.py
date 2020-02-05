from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.

#用户登录
def login(request):
    #返回登录页面
    if request.method == "GET":
        return render(request,"login.html")

    #处理登录请求
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        print("===>", username)
        print("===>", password)
        if username == "" or password == "":
            return render(request, "login.html", {
                "error": "用户名或密码为空！"
            })

        #django auth方法判断用户
        user = auth.authenticate(username=username, password=password)
        print("用户是否存在？", user)

        if user is not None:
            #记录用户登录状态
            auth.login(request, user)
            #重定向到登陆后直接进入项目管理界面
            return HttpResponseRedirect("/manage/")
        else:
            return render(request, "login.html", {
                "error": "用户名或密码错误！"
            })



#退出功能
@login_required
def logout(request):
    #登录时会在数据库创建session，登录时应该将session清除
    auth.logout(request)
    return HttpResponseRedirect("/")