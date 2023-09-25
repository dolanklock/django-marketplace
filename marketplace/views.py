from django.shortcuts import render, redirect
from items.models import Category, Item
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_auth(fn):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return fn(request, *args, **kwargs)
        else:
            return redirect('home')
    return wrapper

def home(request):
    if request.method == "POST":
        username = request.POST["username"]  # getting users input for username
        password = request.POST["password"]  # getting users input for password
        # authenticate user and login if so
        user = authenticate(request, username=username, password=password)  # using imported function to check if username and password are valid
        if user is not None:
            login(request, user)  # this is the function we imported above
            messages.success(request, "Successful Login")
            return redirect('home')
        else:
            messages.success(request, "Invalid username or password. Please try again.")
            return redirect('home')
    else:
        items = Item.objects.filter(is_sold=False)  # filter by is_sold attribute to get all items not sold
        categories = Category.objects.all()
        return render(request, 'home.html', context={'items': items, 'categories': categories})

def contact(request):
    return render(request, 'contact.html', context={})

def logout_user(request):
    logout(request)
    return render(request, 'home.html', context={})