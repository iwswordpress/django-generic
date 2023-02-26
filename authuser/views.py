from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.conf import settings
from .models import User as CustomUser


def registerUser(request):
    user = settings.AUTH_USER_MODEL
    context = {}
    if request.method == "POST":

        print(request.POST)
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        messages.success(request, "Account was created for " + username)

        context = {
            "info": {
                "username": username,
                "email": email,
                "password1": password1,
                "password2": password2,
            }
        }
    return render(request, "authuser/register.html", context)


def loginUser(request):
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = User.objects.get(username=username)
        except:
            print("test")
            # messages.error(request, "Username does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")

        else:
            messages.error(request, "Username OR password is incorrect")

    return render(request, "authuser/login.html")


def logoutUser(request):
    logout(request)
    messages.info(request, "User was logged out!")
    return redirect("home")
