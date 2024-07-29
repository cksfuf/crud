from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100) # 짧은 정보
    content = models.TextField() # 긴 정보