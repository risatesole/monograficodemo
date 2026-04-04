from django.urls import path
from .views import hello_view, employee

urlpatterns = [
    path('hello/', hello_view),
    path('employee',employee),
]
