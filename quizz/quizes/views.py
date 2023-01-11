from django.shortcuts import render
from .models import *
from django.views.generic import ListView

from django.http import JsonResponse
from django.shortcuts import HttpResponse
from Main.models import *
from resultats.models import Resultat



def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

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

def save_quiz_view(request,id):
    # print(request.POST)
    if is_ajax(request=request):
        questions=[]
        data=request.POST
        data_= dict(data.lists())
        data_.pop('csrfmiddlewaretoken')

        for k in data_.keys():
            print('key:',k)
            question=Question.objects.get(texte=k)
            questions.append(question)
        
        print(questions)

        user=request.user
        quiz=Quiz.objects.get(id=id)

        score=0
        multiplier=100/ quiz.nombre_de_question
        resultats=[]
        correct_answer=None

        for q in questions:
            a_selected=request.POST.get(q.texte)
            print('reponse_choisi:',a_selected)

            if a_selected != "":
                question_reponse= Reponse.objects.filter(question=q)
                for a in question_reponse:
                    if a_selected== a.texte:
                        if a.correct:
                            score +=1
                            correct_answer=a.texte

                    else: 
                        if a.correct:
                            correct_answer=a.texte

                resultats.append({str(q):{'reponse_correct':correct_answer, 'reponse_donner':a_selected}})
            else:
                resultats.append({str(q):'Pas de reponse'})
        score_=score*multiplier
        Resultat.objects.create(quiz=quiz, user=user, score=score_)

        if score_>= quiz.score_passe:
            return JsonResponse({"Passer": True, "score":score_, "resultats":resultats})
        else:
            return JsonResponse({'Passer':False, "score":score_, "resultats":resultats})

# def resultat(request):

#     return render(request, 'resultat.html')