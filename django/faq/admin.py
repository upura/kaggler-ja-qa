from django.contrib import admin
from .models import QuestionAnswer


@admin.register(QuestionAnswer)
class QuestionAnswer(admin.ModelAdmin):
    pass
