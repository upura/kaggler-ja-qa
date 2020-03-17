from rest_framework import serializers
from .models import QuestionAnswer


class QuestionAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionAnswer
        fields = ('q_text', 'q_posted_at', 'a_text', 'label')
