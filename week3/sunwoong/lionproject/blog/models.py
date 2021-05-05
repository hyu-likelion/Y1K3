from django.db import models

# Create your models here.
# 클래스의 이름은 DB의 이름하고 동일해야 함
class Blog(models.Model):
    # 각 column을 생성
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()

    # 이후에
    # python manage.py makemigration
    # python manage.py migrate
    # 을 수행해야 함.

    # 관리 사이트에서 제목으로 object을 본다.
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]