from django.urls import path
from .views import QuizListView,quizview



urlpatterns = [
    path('',QuizListView.as_view(), name="main_view"),
    path('<int:id>/',quizview,name='quiz_view')
]
