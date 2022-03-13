from django.contrib.auth import authenticate, login, logout
from django.http import request
from django.shortcuts import redirect, render
from products.models import *
from .forms import *

# Create your views here.

def home(request):

    products = Product.objects.all()

    userform = UserAuthForm()

    if request.method == "POST":
        userform = UserAuthForm(request.POST)
        if userform.is_valid():
            userform.save()
        else:
            print("This got some issues, Fix it asap!...")

    return render(request, "home.html", {'products':products, 'userform':userform} )


def loginit(request):

    if request.method == "POST":
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
        else:
            print("User got some issues,that his daddy needs to resolve!")

    return redirect("/")

def logitout(request):
    
    logout(request)
    return redirect("/")