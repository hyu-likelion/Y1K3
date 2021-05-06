from django.db import models

class Todo(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.item + ' | ' + str(self.completed)
