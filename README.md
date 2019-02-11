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

### アプリケーションをつくる

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

### はじめてのビュー作成

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

---

## はじめての Django アプリ作成、その 2

### Database の設定

SQLite以外のDatabaseを使うにはsettings.pyのDATABASESを編集します.

データベースのテーブルを作成するには、以下のコマンドを実行します.

```
python manage.py migrate
```

migrateコマンドは、settings.pyのINSTALLED_APPSの設定を参照するとともに、DATABASES設定に従って必要なすべてのデータベースのテーブルを作成します.

### モデルの作成

これから開発するPollアプリケーションでは、投票項目 (Question) と選択肢 (Choice) の二つのモデルを作成します.  
Questionには質問事項 (question text) と公開日 (publication date) の情報があります.  
Choiceには選択肢（choice text）と投票数 (vote) という二つのフィールドがあります.  
また、各Choiceは一つのQuestionに関連づけられています.

polls/models.py
```
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

### モデルを有効にする

アプリケーションをプロジェクトに含めるには、構成クラスへの参照を INSTALLED_APPS 設定に追加する必要があります.

mysite/settings.py
```
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

これで Django は、pollsアプリケーションが含まれていることを認識できます. 以下のコマンドも実行しましょう.

```
python manage.py makemigrations polls
```

makemigrations を実行することで、Djangoにモデルに変更があったことを伝えることができます.

マイグレーションはDjangoがモデルやデータベーススキーマの変更を保存する方法です.

【マイグレーションまとめ】
- makemigrations: モデルの変更を適用する.
- migrate: データベースに変更を適用する.
- sqlmigrate: 実際にはデータベースにマイグレーションを実行しない. ただ、Djangoが必要としているSQLが何であるかをスクリーンに表示する.
