from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    # Relationships
    team = models.ForeignKey("Team", on_delete=models.CASCADE, related_name="todos")
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")

    # Status & priority
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=10,
        choices=[
            ("low", "Low"),
            ("medium", "Medium"),
            ("high", "High"),
        ],
        default="medium"
    )

    # Dates
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
    