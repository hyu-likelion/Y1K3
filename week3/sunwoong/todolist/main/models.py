from django.db import models

class Todo(models.Model):
    work = models.CharField(max_length=200)

    def __str__(self):
        return self.work