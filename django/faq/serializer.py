from rest_framework import serializers
from .models import User, QuestionAnswer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name',)


class QuestionAnswerSerializer(serializers.ModelSerializer):
    q_author = UserSerializer()
    a_author = UserSerializer()

    class Meta:
        model = QuestionAnswer
        fields = ('q_text', 'q_posted_at', 'q_author',
                  'a_text', 'a_posted_at', 'a_author',
                  'label', 'slack_url')
