from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def list_case(request):
    return render(request, "case/debug.html")


def send_req(request):
    if request.method == "GET":
        id = request.GET.get("id")
        name = request.GET.get("name")
        return JsonResponse({"status": 10200,
        "message":"success"})