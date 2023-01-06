from django.shortcuts import render
from .models import Quiz
from django.views.generic import ListView

class QuizListView(ListView):
    model=Quiz
    template_name="quizzes/main.html"


def quizview(request, id):
    quiz=Quiz.objects.get(id=id)
    context={
        'obj':quiz,
    }
    return render(request, 'quizzes/quiz.html',context)