from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #return HttpResponse("Welcome to Transflower")
    return render(request, 'HelloApp/home.html')

def about(request):
    #return HttpResponse("Transflower Learning Pvt. Ltd.")
    return render(request, 'HelloApp/about.html')
   
def contact(request):
    #return HttpResponse("Transflower Learning Pvt. Ltd.")
    return render(request, 'HelloApp/contact.html')