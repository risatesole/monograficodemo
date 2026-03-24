from django.shortcuts import render
from app.env import env

def home(request):
    return render(request, "pages/home.html", {
        "title": env["companyname"],
        "slogan": env["slogan"]        
    })
