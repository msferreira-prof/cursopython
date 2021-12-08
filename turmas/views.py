from django.shortcuts import render, redirect
from datetime import datetime 
from professores.models import Professor, Titularidade
from .models import Turma

from .forms import frmTurmaCadastrar

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
    
def consultar(request):
    return render(request, 'turmas/consultar.html')    

def cadastrarTurma(request):
    if request.method == 'POST':
        form = frmTurmaCadastrar(request.POST)
        if form.is_valid():
            
            cd = form.cleaned_data
            
            professor = Professor( 
                            matricula = cd['professor']
            )
            
            turma = Turma (
                        serie = cd['serie'],
                        sala = cd['sala'],
                        horaInicial = cd['horaIncial'],
                        horaFinal = cd['horaFinal'],
                        professor = professor
            )
            
            print(cd['professor'])
            print(cd['horaIncial'])
            print(cd['horaFinal'])
            print(professor)
            
            #turma.save()    
            
            return redirect('/turmas/cadastrar')
    
            
    return redirect('/')

