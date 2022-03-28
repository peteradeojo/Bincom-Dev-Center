from django.db import models
from django.utils import timezone as dj_timezone

# Create your models here.


class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=40, unique=True)
    description = models.TextField()
    status = models.BooleanField(default=False)
    time = models.DateTimeField(default=dj_timezone.now)

    def __str__(self):
        return self.title

    def toggle(self):
      self.status = not self.status
