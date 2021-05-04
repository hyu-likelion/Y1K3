from django.db import models

# Create your models here.


class Survey(models.Model):
    survey_idx = models.AutoField(primary_key=True)

    question=models.TextField(null=True)

    ans1=models.TextField(null=True)
    ans2=models.TextField(null=True)
    ans3=models.TextField(null=True)
    ans4=models.TextField(null=True)


class Answer(models.Model):
    answer_idx = models.AutoField(primary_key=True)

    survey_idx = models.IntegerField()

    ans=models.TextField()