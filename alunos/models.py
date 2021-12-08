from django.db import models
from professores.models import Professor, Titularidade
from turmas.models import Turma

# Create your models here.
class Aluno(models.Model):
    matricula = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=50, blank=False)
    turma = models.ForeignKey(Turma, on_delete=models.DO_NOTHING)
