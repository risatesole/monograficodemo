from django.urls import path
from .views import employeemanager, employee_api

urlpatterns = [
    path("", employeemanager, name="employee"),          # UI
    path("api/", employee_api, name="employee_api"),     # API
]