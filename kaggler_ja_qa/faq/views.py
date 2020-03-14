from rest_framework import viewsets
from .models import User, QuestionAnswer
from .serializer import UserSerializer, QuestionAnswerSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class QuestionAnswerViewSet(viewsets.ModelViewSet):
    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionAnswerSerializer
    filter_fields = ('q_author', 'label')
