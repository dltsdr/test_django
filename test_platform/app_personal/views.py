from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    return render(request,"hello.html")

#用户登录
def login(request):
    return render(request,"login.html", {"error": "登陆页面"})

def login_action(request):
    #登陆动作处理
    print("请求方法：",request.method)
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        print("===>", username)
        print("===>", password)
        if username == "" or password == "":
            return render(request, "login.html", {
                "error": "用户名或密码为空！"
            })
        if username == "zhangsan" and password =="123":
            return render(request, "manage.html", {
                "error": "登陆成功"
            })
        else:
            return render(request, "login.html", {
                "error": "用户名或密码错误！"
            })