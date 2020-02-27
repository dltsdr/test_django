from django.shortcuts import render

# Create your views here.

def list_case(request):
    return render(request, "case/debug.html")