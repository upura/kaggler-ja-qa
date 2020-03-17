from django.db import models


class User(models.Model):
    def __repr__(self):
        return "{}: {}".format(self.pk, self.name)
    __str__ = __repr__

    name = models.CharField(max_length=32)


class QuestionAnswer(models.Model):
    def __repr__(self):
        return "{}: {}".format(self.pk, self.q_text)
    __str__ = __repr__

    LABEL_PROPROCESS = '前処理'
    LABEL_FEATURE_ENGINEERING = '特徴量エンジニアリング'
    LABEL_MODELING = 'モデリング'
    LABELS_SET = (
        (LABEL_PROPROCESS, '前処理'),
        (LABEL_FEATURE_ENGINEERING, '特徴量エンジニアリング'),
        (LABEL_MODELING, 'モデリング')
    )
    q_text = models.TextField()
    q_posted_at = models.DateTimeField()
    a_text = models.TextField()
    label = models.CharField(choices=LABELS_SET, default=LABEL_PROPROCESS, max_length=32)
