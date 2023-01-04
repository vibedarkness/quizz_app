from django.db import models
from quizes.models import Quiz

# Create your models here.

class Question(models.Model):
    texte = models.CharField(max_length = 200)
    quiz=models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=False)
    
    
    def __str__(self):
        return str(self.texte)

    def get_reponses(self):
        return self.reponse_set.all()
        


class Reponse(models.Model):
    texte = models.CharField(max_length = 200)
    correct = models.BooleanField(default=False)
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return f"question:{self.question.texte}, reponse:{self.texte}, correct:{self.correct}"
    
    
   