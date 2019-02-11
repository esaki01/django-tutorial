"""
Applicationもしくは機能ごとに先頭のURLを振り分けることができる.
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]


"""Memo
include() 関数は他のURLのConfigurationへの参照とすることができます.
include() に一致したURLの部分を切り落とし、残りのURLをインクルードされたURLのConfigurationへ渡します.
ここでは、'polls.urls'がインクルードされているので、'polls/'というURLに遭遇したらpolls/urls.pyに処理が渡されます.
"""
