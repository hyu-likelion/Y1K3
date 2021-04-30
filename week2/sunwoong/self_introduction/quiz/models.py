from django.db import models

# ID : admin
# password : admin

# Create your models here.
class Question(models.Model):
    index = models.AutoField(primary_key=True)
    question = models.CharField(max_length=100)
    selection1 = models.CharField(max_length=100)
    selection2 = models.CharField(max_length=100)
    selection3 = models.CharField(max_length=100)
    selection4 = models.CharField(max_length=100)
    selection5 = models.CharField(max_length=100)

    def __str__(self):
        return self.question