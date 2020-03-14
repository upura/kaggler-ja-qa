from django.contrib import admin
from .models import User, QuestionAnswer


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(QuestionAnswer)
class Entry(admin.ModelAdmin):
    pass
