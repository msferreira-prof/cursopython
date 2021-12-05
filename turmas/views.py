from django.shortcuts import render
from professores.models import Professor
from .models import Turma

# Create your views here.
def cadastrar(request):
    professores = Professor.objects.all()
    return render(request, 'turmas/cadastrar.html', {
        'professores': professores
    })

def listar(request):
    turmas = Turma.objects.all()
    return render(request, 'turmas/listar.html', {
        'turmas': turmas
    })
