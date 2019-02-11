"""
管理者画面の設定.
"""

from django.contrib import admin

from .models import Question

admin.site.register(Question)