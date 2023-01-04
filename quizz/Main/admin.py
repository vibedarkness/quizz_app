from django.contrib import admin
from .models import *

# Register your models here.



class AnswerInline(admin.TabularInline):
    model=Reponse

class QuestionAdmin(admin.ModelAdmin):
    inlines=[AnswerInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Reponse)

