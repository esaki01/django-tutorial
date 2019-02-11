# Django Tutorial

## はじめての Django アプリ作成、その 1

### プロジェクトを作成

コマンドラインから、コードを置きたい場所に cd して、以下のコマンドを 実行してください.

```
django-admin startproject project_name
```

以下のようなディレクトリが作成されます.

```
project_name/
    manage.py
    project_name/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

- manage.py: Djangoプロジェクトに対する様々な操作を行うためのもの.  
- settings.py: Djangoプロジェクトの設定ファイル.  
- urls.py: DjangoプロジェクトのURL宣言. Djangoサイトにおける「目次」に相当.  
- wsgi.py: プロジェクトをサーブするためのWSGI互換Webサーバーとのエントリーポイント.

Django のプロジェクトがうまく動作するか確認しましょう.

```
python manage.py runserver
```

## アプリケーションをつくる

manage.pyと同じディレクトリにフォルダを作成しましょう.

```
python manage.py startapp app_name
```

中身はこのようになっています.

```
app_name/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```





