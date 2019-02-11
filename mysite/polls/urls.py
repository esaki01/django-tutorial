"""
ApplicationのURLを宣言する. URLのConfiguration.
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]


"""Memo
path(route, view, kwargs, name)の引数について.

route: URLパターンを含む文字列.
view: View関数を指定する.
kwargs: 任意のキーワード引数を辞書として対象のビューに渡せる.
name: URLに名前付けする. Djangoのどこからでも明確に参照できるようになる.
"""
