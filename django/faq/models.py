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

    LABEL_PROPROCESS = 'preprocessing'
    LABEL_FEATURE_ENGINEERING = 'feature_engineering'
    LABEL_MODELING = 'modeling'
    LABELS_SET = (
        (LABEL_PROPROCESS, '前処理'),
        (LABEL_FEATURE_ENGINEERING, '特徴量エンジニアリング'),
        (LABEL_MODELING, 'モデリング')
    )
    q_text = models.TextField()
    q_posted_at = models.DateTimeField(auto_now_add=True)
    q_author = models.ForeignKey(User, related_name='questions', on_delete=models.CASCADE)
    a_text = models.TextField()
    a_posted_at = models.DateTimeField(auto_now_add=True)
    a_author = models.ForeignKey(User, related_name='answers', on_delete=models.CASCADE)
    label = models.CharField(choices=LABELS_SET, default=LABEL_PROPROCESS, max_length=32)
    slack_url = models.URLField(default='')
