# 시작
1. 프로젝트 생성
- 폴더 생성 후 들어가서 code로 열기
```bash
django-admin startproject crud .
```

2. 가상환경 생성
```bash
python -m venv venv
```

3. 가상환경 활성화
```bash
source venv/Scripts/activate
```

4. 가상환경 내부에 django 설치
```bash
pip install django
```

5. 앱생성
```bash
django-admin startapp posts
```

6. git init 관리
- git init 후 구글에 gitignore.io 검색
- python, VisualStudioCode, windows, macOS, Django 생성
- code로 돌아와 .gitignore 파일 만들고 생성된 코드 붙여넣기

7. 서버 실행(서버 종료는 ctrl+c)
- 실행후 나오는 주소 (예를들어 http://127.0.0.1:8000/ 에 ctrl+클릭하면 이동됨.)
```bash
python manage.py runserver
```

8. templates 폴더 생성.
- 4번에서 생성한 `posts` 폴더에 마우스 우클릭 하고 `templates` 폴더 생성.
- html 파일 관리 장소

9. app 등록
- 1번에서 생성한`crud` > `setting.py` 찾아 들어가기
- 33번 줄 `INSTALLED_APPS`에 우리가 만든 `posts` 등록하기
```python
INSTALLED_APPS = [
    ...
    'posts'
]
```

10. index 페이지 구성
- `crud` > `urls.py` 들어가기
- 18번 줄 아래 `from posts import views`(`posts`을 지정해주기)
- 20번 줄의 `urlpatterns`에 코드 작성

```python
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
]
```

11. 로직 정의
- 애플리케이션에서 요청을 처리하는 로직을 정의하는 파일
- `posts` > `views.py` 파일 찾아 들어가기
- 여기에 `urls.py` 에서 지정한 로직정의하는 함수 만들기
```python
def index(request):
    return render(request, 'index.html')
```

# Model

1. 모델 정의
- `posts` > `models.py`에 클래스 정의
```python
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100) # 짧은 정보
    content = models.TextField() # 긴 정보
```

2. 번역본 생성
- python에서 작성한 models.py 코드를 sql 언어로
- 실행중인 서버 종료(ctrl + c) 후 코드 입력
```bash
python manage.py makemigrations
```

3. DB에 반영
```bash
python manage.py migrate
```

4. superuser 생성
- 아이디 비번 만드는 코드
- 아이디: `admin`, 이메일은 넘어가고 비번: `입력`(비번은 표시안됨)
```bash
python manage.py createsuperuser
```

5. admin 에 모델 등록
```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```


# 기능 구현

## 1. Read(All) 구현
- `templates` > `index.html` 파일 만들기
- `index.html` 파일에 반복문 설정
- `posts` > `views.py`에 import 와 함수 추가
```html
 <!--
 posts > templates > index.html
 -->
<body>
    <h1>여기는 index 입니다.</h1>
    
    {% for post in posts %}
        <p>{{post.title}}</p>
        <p>{{post.content}}</p>
    {% endfor %}
</body>
```
```python
# posts > views.py
from .models import Post

def index(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'index.html', context)
```

## 2. Read(1) 구현
- `crud` > `urls.py` 에 `path('posts/<int:id>/', views.detail)` 추가
- `posts` > `templates` > `detail.html` 파일 추가
- `posts` > `templates` > `index.html` 파일 수정
-  `posts` > `views.py` 에 `detail` 함수 작성

```python
# crud > urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    # 추가
    path('posts/<int:id>/', views.detail),
]
```
```html
<!--
 posts > templates > detail.html
 -->
<body>
    <h1>detail</h1>
    <h2>{{post.title}}</h2>
    <p>{{post.content}}</p>
</body>
```
```html
<!--
 posts > templates > index.html
 -->
<body>
    <h1>여기는 index 입니다.</h1>
    
    {% for post in posts %}
        <p>{{post.title}}</p>
        <a href="/posts/{{post.id}}/">detail</a>
        <hr>
    {% endfor %}
</body>
```
```python
def detail(request, id):
    post = Post.objects.get(id=id)

    context = {
        'post': post,
    }

    return render(request, 'detail.html', context)
```


## 3. Creat 기능 구현
- `crud` > `urls.py` 에 `path('posts/new/', views.new), path('posts/create/', views.create),` 추가
- `posts` > `templates` > `detail.html` 수정(home으로 가기 추가)
- `posts` > `templates` > `index.html` 수정(creat 기능 추가)
- `posts` > `templates` > `new.html` 생성
- `posts` > `views.py` import 와 함수 추가
```python
# crud > urls.py
urlpatterns = [
    ...
    path('posts/<int:id>/', views.detail),

    # Create 추가
    path('posts/new/', views.new),
    path('posts/create/', views.create),
]
```
```html
<!--
 posts > templates > detail.html
 -->
<body>
    <h1>detail</h1>
    <h2>{{post.title}}</h2>
    <p>{{post.content}}</p>
    <hr>
    <a href="/">home</a>
</body>
```
```html
<!--
 posts > templates > index.html
 -->
<body>
    <h1>여기는 index 입니다.</h1>
    
    {% for post in posts %}
        <p>{{post.title}}</p>
        <!--추가-->
        <a href="/posts/{{post.id}}/">detail</a>
        <hr>
    {% endfor %}
</body>
```
```html
<!--
 posts > templates > new.html
 -->
<body>
    <form action="/posts/create/">
        <label for="title">Title: </label>
        <input type="text" id="title" name="title">

        <label for="content">Content: </label>
        <input type="text" id="content" name="content">

        <input type="submit">
    </form>
</body>
```
```python
# posts > views.py
# redirect 추가
from django.shortcuts import render, redirect

# 함수 추가
def new(request):
    return render(request, 'new.html')


def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    post = Post()
    post.title = title
    post.content = content
    post.save()

    return redirect(f'/posts/{post.id}/')
```

4. Delet 기능 구현