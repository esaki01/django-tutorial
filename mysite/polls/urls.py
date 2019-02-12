"""
ApplicationのURLを宣言する. URLのConfiguration.
"""

from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]


"""Memo
path(route, view, kwargs, name)の引数について.

route: URLパターンを含む文字列.
view: View関数を指定する.
kwargs: 任意のキーワード引数を辞書として対象のビューに渡せる.
name: URLに名前付けする. Djangoのどこからでも明確に参照できるようになる.
"""
