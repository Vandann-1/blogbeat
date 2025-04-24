from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User   # Import User model from Django's auth module
from blogapp.models import Blog
from django.contrib import messages


def register(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.create_user(
            username=email, first_name=firstname, last_name=lastname, password=password
        )
        user.save()
        return redirect("login")  # Fix redirect URL
    return render(request, "registers.html")



def home(request):
    blogs = Blog.objects.all()
    
    # Attach 'is_saved' attribute for each blog
    # for blog in blogs:
        # blog.is_saved = request.user.is_authenticated and blog.saved_by.filter(id=request.user.id).exists()
    return render(request, "home.html", {"blogs": blogs})


def loginview(request):
    if request.user.is_authenticated:   
        return redirect("home")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")  # Redirect to home after successful login
        else:
            messages.error(request,"invalid email or password. ")
            return redirect("login")  # Fix redirect loop issue

    return render(request, "login.html")


@login_required(login_url="login")  # Redirect to login page if not authenticated
def logoutview(request):
    logout(request)
    return redirect("login")  # Redirect to login page after logout


def Settings(request):
    if request.user.is_authenticated:
        return render(request, "settings.html")
    return redirect("login")

def helSupport(request):
    return render(request, "helpsupport.html")

def hh(request):
    return render (request, "h.html")
    



    
    
           