from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Hello!")

def voight(request): 
    return HttpResponse("Hello, voight!")

def pals(request):
    return HttpResponse("Hello, pals!")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}")