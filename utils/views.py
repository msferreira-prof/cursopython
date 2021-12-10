from django.shortcuts import render, redirect
from datetime import datetime
from professores.models import Professor, Titularidade
from turmas.models import Turma
from alunos.models import Aluno

# Create your views here.
def carregar(request):
    # titularidade
    for n in range(0, 2):
        nomeTitularidade = "Titularidade_" + str(n + 1)
        titularidade = Titularidade( 
            nome = nomeTitularidade
        )

        titularidade.save()
    
    # professores
    for n in range(0, 2):
        nomeProf = "Professor_" + str(n + 1)
        titularidade = Titularidade.objects.get(pk=n+1)
        
        professor = Professor( 
            nome = nomeProf,
            titularidade = titularidade 
        )

        professor.save()
    
    # turmas
    for n in range(0, 2):
        nomeTurma = "Turma_" + str(n + 1)
        professor = Professor.objects.get(pk=n+1)
        
        turma = Turma (
            serie = (n + 1),
            sala = (101 + n),
            horaInicial = datetime.now().time(),
            horaFinal = datetime.now().time(),
            professor = professor
        )

        turma.save()

    # alunos
    for n in range(0, 2):
        nomeAluno = "Aluno_" + str(n + 1)
        turmaAluno = Turma.objects.get(pk=n+1)
        aluno = Aluno (
            nome = nomeAluno,
            turma = turmaAluno
        )

        aluno.save()

    return redirect('/')