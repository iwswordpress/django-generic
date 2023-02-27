from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from .models import User

""" 
Registration and loginfunctions.
We are using the Custom User model from authuser.models.
User is registered and we will have an automatic Profile created through signals.py
"""


def registerUser(request):
    """
    Receive POST data from register page.
    We do not need username, so register from can have username field removed.
    """

    context = {}
    if request.method == "POST":

        print(request.POST)
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        # new_user.create_user(CustomUser, email, password1)
        # User.objects.create_user("lennon@thebeatles.com", "johnpassword")
        try:
            User.objects.create_user(email, password1)
        except:
            print("Error registering user.")
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
    """Login user withemail and password as this has been defined in Custom User model."""
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
