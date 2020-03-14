from rest_framework import routers
from .views import UserViewSet, QuestionAnswerViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'qa', QuestionAnswerViewSet)
