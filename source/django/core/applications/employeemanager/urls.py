from django.urls import path
from .views import teambase, create_team

urlpatterns = [
    path("", teambase, name="teambase"),
    path("createteam/", create_team, name="createteam"),
]
