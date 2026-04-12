from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from applications.account.server.handlers.signin import signinHandler

def signup(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(email=email).exists():
            messages.error(request, "User with this email already exists.")
        else:
            user = User.objects.create_user(
                username=email,  # 👈 use email as username
                email=email,
                password=password,
                first_name=firstname,
                last_name=lastname
            )
            messages.success(request, "Account created successfully!")
            login(request, user)
            return redirect("/app/")

    return render(request, "signup_ES.html", {"title": "Teambase"})


def signin(request):
    response = signinHandler(request)
    if response:
        return response
    return render(request, "signin_ES.html", {"title": "Teambase"})

@login_required
def profile(request):
    return render(request, "profile.html", {
        "user": request.user,
        "title": "Profile"
    })

def signout(request):
    logout(request)
    return redirect("/signin/")