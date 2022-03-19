from django.db import models

# Create your models here.
class TaskList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'

class Task(models.Model):
    tasklist = models.ForeignKey('TaskList', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    deadline_date = models.DateField()

    def __str__(self):
        return f'{self.name}'