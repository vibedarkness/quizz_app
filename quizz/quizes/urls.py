from django.urls import path
from .views import QuizListView,quizview,quiz_data_view



urlpatterns = [
    path('',QuizListView.as_view(), name="main_view"),
    path('<int:id>/',quizview,name='quiz_view'),
    path('<int:id>/donnée/', quiz_data_view ,name='quiz_data_view')
]
