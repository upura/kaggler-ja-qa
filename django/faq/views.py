from rest_framework import viewsets
from .models import QuestionAnswer
from .serializer import QuestionAnswerSerializer


class QuestionAnswerViewSet(viewsets.ModelViewSet):
    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionAnswerSerializer
    filter_fields = ('label',)
