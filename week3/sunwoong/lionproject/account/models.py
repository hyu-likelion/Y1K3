from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# 장고에서 제공하는 모델 상속
class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=100)
    university = models.CharField(max_length=50)
    location = models.CharField(max_length=200)