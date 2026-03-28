from django.shortcuts import render
from applications.employeemanager.server.handlers.employeeHandler import employeeHandler

# 🔹 UI view (ONLY HTML)
def employeemanager(request):
    return render(request, "employeemanager/employeemanager.html", {
        "title": "AvantKeel"
    })

# 🔹 API view (ONLY JSON)
def employee_api(request):
    return employeeHandler(request)