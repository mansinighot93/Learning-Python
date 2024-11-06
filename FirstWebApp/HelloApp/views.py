from django.shortcuts import render
from django.http import HttpResponse

from .models import Customer, Product
from .forms import LoginForm,RegisterForm

def home(request):
    #return HttpResponse("Welcome to Transflower")
    return render(request, 'HelloApp/home.html')

def about(request):
    #return HttpResponse("Transflower Learning Pvt. Ltd.")
    return render(request, 'HelloApp/about.html')
   
def contact(request):
    #return HttpResponse("Transflower Learning Pvt. Ltd.")
    return render(request, 'HelloApp/contact.html')

def login(request):
    return render(request,'HelloApp/login.html')

def catalog(request):
    products = [
    {"name": "Laptop", "description": "A high-performance laptop", "price": 999.99},
    {"name": "Smartphone", "description": "A latest-generation smartphone", "price": 699.99},
    {"name": "Headphones", "description": "Noise-cancelling over-ear headphones", "price": 199.99},
    {"name": "Keyboard", "description": "Mechanical keyboard with RGB lighting", "price": 129.99},
    {"name": "Mouse", "description": "Wireless ergonomic mouse", "price": 49.99}
    ]
    return render(request, 'HelloApp/list.html',{'products': products})

def flowers(request):
    flowers = [
        Product("Gerbra", "Wedding Flower", 45.5),
        Product("Rose", "Valentine Flower", 65),
        Product("Jasmine","Smelling Flower", 23),
        Product("Lily", "Delicate Flower", 76),
        Product("Lotus", "worship", 12),
    ]
    return render(request, 'HelloApp/list.html',{'products': flowers})

def customers(request):

    customer=Customer("Sachin", "sachin.t@gmail.com", "988767654")

    customers = [
    Customer("Sachin", "sachin.t@gmail.com", "988767654"),
    Customer("Ravi", "sachin.t@gmail.com", "988767654"),
    Customer("Manish", "sachin.t@gmail.com", "988767654"),
    Customer("Sarang", "sachin.t@gmail.com", "988767654"),
    Customer("Seema", "sachin.t@gmail.com", "988767654"),
    ]

    return render(request, 'HelloApp/customers.html',{'customers': customers})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            return render(request,'HelloApp/welcome.html',{'password':password,'email':email})
    else:
        form = LoginForm()
    return render(request,'HelloApp/login.html',{'form':form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            location = form.cleaned_data['location']
            contactnumber = form.cleaned_data['contactnumber']
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']

            return render(request,'HelloApp/welcome.html',{'email':email,'password':'manasi'})
    else:
        form = RegisterForm()
    return render(request,'HelloApp/register.html',{'form':form})