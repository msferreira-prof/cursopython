from django.db import models
from django.utils import timezone
from professores.models import Professor

# Create your models here.
class Turma(models.Model):
    codigo = models.BigAutoField(primary_key=True)
    serie = models.CharField(max_length=10, blank=False)
    sala = models.IntegerField(blank=False)
    horaInicial = models.TimeField(blank=False, default=timezone.now)
    horaFinal = models.TimeField(blank=False, default=timezone.now)
    professor = models.ForeignKey(Professor, on_delete=models.DO_NOTHING)