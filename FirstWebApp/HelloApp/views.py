from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome To Transflower")

def about(request):
    return HttpResponse("Transflower pvt.ltd")

def contact(request):
    return HttpResponse("Manchar")

    


