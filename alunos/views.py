from django.shortcuts import render, redirect
from professores.models import Professor, Titularidade
from turmas.models import Turma
from .models import Aluno
from .forms import frmAlunoCadastrar

# Create your views here.
def cadastrar(request):
    turmas = Turma.objects.all()
    return render(request, 'alunos/cadastrar.html', {
        'turmas': turmas
    })

def listar(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos/listar.html', {
        'alunos': alunos
    })
    
def consultar(request):
    return render(request, 'alunos/consultar.html')    

def cadastrarAluno(request):
    if request.method == 'POST':
        form = frmAlunoCadastrar(request.POST)
        if form.is_valid():
            
            cd = form.cleaned_data
            
            turma = Turma(
                        codigo = cd['turma']    
            )
            
            aluno = Aluno(
                    nome = cd['nomeAluno'],
                    turma = turma
                    #cd['fotoProfessor']
            )
    
            aluno.save()

            return redirect('/alunos/cadastrar')
        
    return redirect('/')

def excluir(request, pk):
    aluno = Aluno.objects.get(pk=pk)
    aluno.delete()
    return redirect('/alunos/listar')

def atualizar(request, pk):
    aluno = Aluno.objects.get(pk=pk)
    return render(request, 'alunos/atualizar.html')
