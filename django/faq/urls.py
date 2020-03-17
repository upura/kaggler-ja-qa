from rest_framework import routers
from .views import QuestionAnswerViewSet


router = routers.DefaultRouter()
router.register(r'qa', QuestionAnswerViewSet)
