from django.db import models
from django.contrib.auth import get_user_model
from core.events.models import Event

# Create your models here.
User = get_user_model()


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField()
    priority = models.CharField(
        max_length=255,
        choices=[("low", "Low"), ("medium", "Medium"), ("high", "High")],
        default="medium",
        db_index=True,
    )
    status = models.CharField(
        max_length=255,
        choices=[
            ("todo", "Todo"),
            ("in-progress", "In Progress"),
            ("done", "Done"),
        ],
        default="todo",
        db_index=True,
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="tasks",
    )
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="task_assigned",
    )
    is_completed = models.BooleanField(default=False)  # type: ignore
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"
