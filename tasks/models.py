from django.db import models
from django.conf import settings

# Create your models here.
USER_MODEL = settings.AUTH_USER_MODEL


class Task(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField(null=False)
    due_date = models.DateTimeField(null=False)
    is_completed = models.BooleanField(default=False)
    project = models.ForeignKey(
        "projects.Project",
        related_name="tasks",
        on_delete=models.CASCADE,
    )
    assignee = models.ForeignKey(
        USER_MODEL, related_name="tasks", on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.name
