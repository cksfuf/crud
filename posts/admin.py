from django.contrib import admin
from .models import Post # .models 는 현재 나와 똑같은 위치에 있는 파일

# Register your models here.
admin.site.register(Post) # potst 라는 모델 등록