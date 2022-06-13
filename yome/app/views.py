from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

def signup(request):
    return render(request, "app/index.html")

def login(request):
    return render(request,  "app/login.html")
def acc(request):
    return render(request, "app/acc.html")
    