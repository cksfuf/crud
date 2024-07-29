# Model

1. 모델 정의
```python
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100) # 짧은 정보
    content = models.TextField() # 긴 정보
```

2. 번역본 생성
- python에서 작성한 models.py 코드를 sql 언어로
```bash
python manage.py makemigrations
```