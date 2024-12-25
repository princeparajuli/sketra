

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def register(request):
    return render(request, 'register.html')

def houseplan(request):
    return render(request,'houseplan.html')

def registerpg(request):
    return render(request,"registerpg.html")
