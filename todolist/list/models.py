from django.db import models

# Create your models here.
class ToDoList(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    done = models.BooleanField()

    def __str__(self):
        return self.title

