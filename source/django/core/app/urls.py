# app/urls.py
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from applications.core.views import home
from applications.employeemanager.views import employeemanager

def applicationPage(request):
    return render(request, 'pages/app.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('app/', employeemanager),
    path('', include('applications.account.urls')),  # handles signup/signin
]