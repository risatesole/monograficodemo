from django.shortcuts import render , redirect
from applications.employeemanager.server.handlers.employeeHandler import employeeHandler
from django.contrib.auth.decorators import login_required
from .models import Employee


@login_required
def employeemanager(request):
    if request.method == "POST":
            # Employee.objects.create(
            #     firstname=request.POST.get("fname"),
            #     lastname=request.POST.get("lname"),
            #     role=request.POST.get("role"),
            #     email=request.POST.get("email"),
            #     submitted_by=request.user             
            # )

            print(f"signed user: {request.user}")
            print(f"first name: {request.POST.get("fname")}")
            print(f"last name: {request.POST.get("lname")}")
            print(f"role: {request.POST.get("role")}")
            print(f"email: {request.POST.get("email")}")

            # employees = Employee.objects.filter(submitted_by=request.user)


    return render(request, "employeemanager/employeemanager.html", {
        "title": "AvantKeel"
    })
