from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "hello/index.html")

def voight(request): 
    return HttpResponse("Hello, voight!")

def pals(request):
    return HttpResponse("Hello, pals!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })