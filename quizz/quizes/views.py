from django.shortcuts import render
from .models import *
from django.views.generic import ListView

from django.http import JsonResponse

class QuizListView(ListView):
    model=Quiz
    template_name="quizzes/main.html"


def quizview(request, id):
    quiz=Quiz.objects.get(id=id)
    context={
        'obj':quiz,
    }
    return render(request, 'quizzes/quiz.html',context)


def quiz_data_view(request, id):
    quiz=Quiz.objects.get(id=id)
    questions=[]

    for q in quiz.get_questions():
        reponses=[]
        for r in q.get_reponses():
            reponses.append(r.texte)
        questions.append({str(q):reponses})
    return JsonResponse({
        'data':questions,
        'time':quiz.temps,
        
    })