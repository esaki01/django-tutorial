# Django Tutorial

https://docs.djangoproject.com/ja/2.1/intro/

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

### 管理ユーザーを作成する

adminサイトにログインできるユーザーを作成します.

```
python manage.py createsuperuser
```

好きなユーザー名を入力しEnterを押す.

```
Username: admin
```

希望するemailアドレスを入力するよう促される.

```
Email address: admin@example.com
```

パスワードも.

```
Password: **********
Password (again): *********
Superuser created successfully.
```

### 開発サーバーの起動

```
python manage.py runserver
```

http://127.0.0.1:8000/admin/ にアクセスします.

Pollアプリがまだ編集できないはずです.

### Pollアプリをadmin上で編集できるようにする

polls/admin.py
```
from django.contrib import admin

from .models import Question

admin.site.register(Question)
```

再び、 http://127.0.0.1:8000/admin/ にアクセスすると、Pollアプリが編集できるようになっています.
もしできない場合は、マイグレーションをしましょう.

---

## はじめての Django アプリ作成、その 3

### テンプレートを作成する

polls/templates/polls/index.htmlを作成します.

テンプレートの設定は、setting.pyのTEMPLATES にあります.

#### 参考 - テンプレートの名前空間

作ったテンプレートを polls という別のサブディレクトリを作らずに、直接 polls/templates の中に置いてもいいのではないか、と思うかもしれませんね。しかし、それは実際には悪い考えです。Django は、名前がマッチした最初のテンプレートを使用するので、もし 異なる アプリケーションの中に同じ名前のテンプレートがあった場合、Django はそれらを区別することができません。そのため、Django に正しいテンプレートを教えてあげる必要がありますが、一番簡単な方法は、それらに 名前空間を与える ことです。アプリケーションと同じ名前をつけた もう一つの ディレクトリの中にテンプレートを置いたのは、そういうわけなのです。

polls/templates/polls/index.html
```
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```

### ビューを更新する

テンプレートをロードしてコンテキストに値を入れ、テンプレートをレンダリングした結果を HttpResponse オブジェクトで返す、というイディオムは非常によく使われます。 Django はこのためのショートカットを提供します.

polls/views.py
```
from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
```

render() 関数は、第1引数として request オブジェクトを、第2引数としてテンプレート名を、第3引数（任意）として辞書を受け取ります. この関数はテンプレートを指定のコンテキストでレンダリングし、その HttpResponse オブジェクトを返します.

### 404 エラーの送出

オブジェクトが存在しない場合には Http404 を送出することは非常によく使われるイディオムです. Django はこのためのショートカットを提供しています.
次のdetail viewでは、リクエストしたIDを持つ質問が存在しないときにHttp404を送出します.

polls/views.py
```
from django.shortcuts import get_object_or_404, render

from .models import Question
# ...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
```

polls/templates/polls/detail.html
```
<h1>{{ question.question_text }}</h1>
<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }}</li>
{% endfor %}
</ul>
```

### テンプレート内のハードコードされたURLを削除

polls/index.htmlテンプレートでリンクの一部は次のようにハードコードされていました.

```
<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
```

これでは、URLの変更が困難になってしまいます. しかし、 polls.urlsファイルで、path() 関数でname引数を定義したので、テンプレートタグの {％url％} を使用して、URL設定で定義されている特定のURLパスへの依存をなくすことができます.

```
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```

### URL名の名前空間

このプロジェクトが持つアプリはpollsアプリ1つだけです. 実際の Django プロジェクトでは、5個、10個、20個、あるいはそれ以上のアプリがあるかもしれません. polls/urls.py ファイル内でapp_nameを追加し、アプリケーションの名前空間を設定してください. また、templateも修正します.

polls/urls.py
```
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```

polls/templates/polls/index.html
```
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
```

---

## はじめての Django アプリ作成、その 4

### フォームを書く

polls/templates/polls/detail.html
```
<h1>{{ question.question_text }}</h1>

{% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

<form action="{% url 'polls:vote' question.id %}" method="post">
{% csrf_token %}
{% for choice in question.choice_set.all %}
    <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
    <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
{% endfor %}
<input type="submit" value="Vote">
</form>
```

polls/views.py
```
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question
# ...
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
```

polls/results.html
```
<h1>{{ question.question_text }}</h1>

<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }} -- {{ choice.votes }} vote{{ choice.votes|pluralize }}</li>
{% endfor %}
</ul>

<a href="{% url 'polls:detail' question.id %}">Vote again?</a>
```

### 汎用ビューを使う

これまで作成してきたpollアプリを汎用ビューシステムに変換して、コードをばっさり捨てられるようにしましょう. 変換にはほんの数ステップしかかかりません. 

Step
- URLconf を変換する.
- 古い不要なビューを削除する.
- 新しいビューに Djangoの汎用ビューを設定する.

polls/urls.py
```
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```

polls/views.py
```
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    ... # same as above, no changes needed.
```

---

## はじめての Django アプリ作成、その 5

### 初めてのテスト作成

以下のメソッドを追加してテストを実施します.

polls/models.py
```
def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now
```

polls/tests.py
```
import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
        
    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)
        
    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)
```

```
python manage.py test polls
```

### ビューをテストする

現在の投票のリストは、まだ公開されていない (つまり pub_date の日付が未来になっている) 投票が表示される状態になっています. これを直しましょう.

polls/views.py
```
from django.utils import timezone

def get_queryset(self):
    """
    Return the last five published questions (not including those set to be
    published in the future).
    """
    return Question.objects.filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:5]
```

polls/tests.py
```
from django.urls import reverse
```

detailviewにも同様の制約を加えます.

polls/views.py
```
class DetailView(generic.DetailView):
    ...
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
```

polls/tests.py
```
class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """
        future_question = create_question(question_text='Future question.', days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        past_question = create_question(question_text='Past Question.', days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
```

---

## はじめての Django アプリ作成、その 6

### 静的ファイルの管理

polls/static/polls/style.css
```
li a {
    color: green;
}
```

polls/templates/polls/index.html
```
{% load static %}

<link rel="stylesheet" type="text/css" href="{% static 'polls/style.css' %}">
```

画像はpolls/static/polls/images/background.gifに置きます.

polls/static/polls/style.css
```
body {
    background: white url("images/background.gif") no-repeat;
}
```

---

## はじめての Django アプリ作成、その 7

admin フォームの表示方法や操作の仕方をデフォルトから変更したいこともよくあります. それには、オブジェクトを登録する時にオプションを指定します.

polls/admin.py
```
from django.contrib import admin

from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)
```

このように、モデルの admin のオプションを変更したいときには、モデルごとに admin クラスを作成して、 admin.site.register() の 2 番目の引数に渡すと いうパターンに従ってください.

上の例では、「Publication date」フィールドの表示位置を「Question」フィールドよりも前に変更しています.

また、数十ものフィールドがある場合、フォームを複数のフィールドセットに分割したいこともあるでしょう.

polls/admin.py
```
from django.contrib import admin

from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Question, QuestionAdmin)
```



