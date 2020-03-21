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

    LABEL_EDA = '探索的データ分析'
    LABEL_FEATURE_ENGINEERING = '特徴量エンジニアリング'
    LABEL_MODELING = 'モデリング'
    LABEL_VALIDATION = '検証'
    LABEL_ENSEMBLE = 'アンサンブル'
    LABEL_OTHERS = 'その他'

    LABELS_SET = (
        (LABEL_EDA, '探索的データ分析'),
        (LABEL_FEATURE_ENGINEERING, '特徴量エンジニアリング'),
        (LABEL_MODELING, 'モデリング'),
        (LABEL_VALIDATION, '検証'),
        (LABEL_ENSEMBLE, 'アンサンブル'),
        (LABEL_OTHERS, 'その他'),
    )
    q_text = models.TextField()
    q_posted_at = models.DateField()
    a_text = models.TextField()
    label = models.CharField(choices=LABELS_SET, default=LABEL_OTHERS, max_length=32)
