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

3. DB에 반영
```bash
python manage.py migrate
```

4. superuser 생성
```bash
python manage.py createsuperuser
```

5. admin 에 모델 등록
```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```