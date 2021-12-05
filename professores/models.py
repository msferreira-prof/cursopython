from django.db import models
from django.utils import timezone

# Create your models here.
class Titularidade(models.Model):
    codigo = models.BigAutoField(primary_key=True)
    nome = nome = models.CharField(max_length=40, blank=False)
class Professor(models.Model):
    matricula = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=40, blank=False)
    foto = models.CharField(max_length=100, blank=False)
    titularidade = models.ForeignKey(Titularidade, on_delete=models.DO_NOTHING)

