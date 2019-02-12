"""
管理者画面の設定.
"""

from django.contrib import admin

from .models import Choice, Question

admin.site.register(Choice)
admin.site.register(Question)
