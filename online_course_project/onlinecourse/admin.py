from django.contrib import admin
from .models import Course, Question, Choice, Submission

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(Course)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
