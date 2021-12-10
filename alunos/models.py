from django.db import models
from django.db.models.deletion import SET_NULL
from professores.models import Professor, Titularidade
from turmas.models import Turma

# Create your models here.
class Aluno(models.Model):
    matricula = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=50, blank=False)
    turma = models.ForeignKey(Turma, models.SET_NULL, blank=True, null=True)
