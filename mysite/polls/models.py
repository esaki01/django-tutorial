"""
モデルの定義.
"""

from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    # Questionとのリレーションシップを定義する
    # on_delete=models.CASCADEでQuestionが削除されたらそれに紐づくChoiceも削除される
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


"""
question_text, pub_dateなどは、データベースのカラム名にもなる.
"""
