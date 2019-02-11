# Django Tutorial

## はじめての Django アプリ作成、その 1

### プロジェクトを作成

コマンドラインから、コードを置きたい場所に cd して、以下のコマンドを 実行してください.

```
django-admin startproject mysite
```

以下のようなディレクトリが作成されます.

```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

- manage.py: Djangoプロジェクトに対する様々な操作を行うためのもの.  
- settings.py: Djangoプロジェクトの設定ファイル.  
- urls.py: DjangoプロジェクトのURL宣言. Djangoサイトにおける「目次」に相当.  
- wsgi.py: プロジェクトをサーブするためのWSGI互換Webサーバーとのエントリーポイント.

Djangoのプロジェクトがうまく動作するか確認しましょう.

```
python manage.py runserver
```

## アプリケーションをつくる

manage.pyと同じディレクトリにフォルダを作成しましょう.

```
python manage.py startapp polls
```

中身はこのようになっています.

```
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

## はじめてのビュー作成

polls/views.py
```
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

ビューを呼ぶために、URLを対応付けしてやる必要があります.  
そのためにurls.pyというファイルを作ります.

polls/urls.py
```
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

次に、ルートのurls.pyに polls.urlsモジュールの記述を反映させます.

mysite/urls.py
```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

ブラウザで http://localhost:8000/polls/ にアクセスすると、"Hello, world. You're at the polls index." と表示されるのが確認できるでしょう.
