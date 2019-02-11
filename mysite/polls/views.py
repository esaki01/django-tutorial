"""
Applicationに表示するViewを決めるファイル.
viewsを呼ぶために、urlsでURLを対応付ける必要がある.
"""

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
