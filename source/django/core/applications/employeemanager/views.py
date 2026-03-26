from django.shortcuts import render


def employeemanager(request):
    context = {
        "title": "AvantKeel"
    }
    return render(request, 'employeemanager/employeemanager.html', context)