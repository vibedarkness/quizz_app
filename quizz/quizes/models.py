from django.db import models
import random

# Create your models here.

NIVEAU=(
    ('facile','facile'),
    ('moyen','moyen'),
    ('difficile','difficile'),
)

class Quiz(models.Model):
    name = models.CharField(max_length = 120)
    topic = models.CharField(max_length = 120)
    nombre_de_question=models.IntegerField()
    temps=models.IntegerField(help_text="temps du quiz en minutes")
    score_passe=models.IntegerField(help_text="score demander en %")
    niveau = models.CharField(max_length = 15, choices=NIVEAU)
    
    def __str__(self):
        return f"{self.name}-{self.topic}"

    def get_questions(self):
        questions=list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.nombre_de_question]
    
    
    