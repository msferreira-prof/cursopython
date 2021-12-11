from django.db.models.deletion import SET_NULL
from django.db.models.fields import NullBooleanField
from django.shortcuts import render, redirect
from datetime import datetime
import professores 
from professores.models import Professor, Titularidade
from .models import Turma

from .forms import frmTurmaAtualizar, frmTurmaCadastrar

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
            
            if cd['professor'] <= 0:
                professor = None
            else:
                professor = Professor( 
                            matricula = cd['professor']
                )
            
            turma = Turma (
                        serie = cd['serie'],
                        sala = cd['sala'],
                        horaInicial = cd['horaInicial'],
                        horaFinal = cd['horaFinal'],
                        professor = professor
            )
            
            turma.save()    
            
            return redirect('/turmas/cadastrar')
    
            
    return redirect('/')

def excluir(request, pk):
    turma = Turma.objects.get(pk=pk)
    turma.delete()
    return redirect('/turmas/listar')

def atualizar(request, pk):
    professores = Professor.objects.all()
    turma = Turma.objects.get(pk=pk)
    return render(request, 'turmas/atualizar.html',
        {'turma': turma, 'professores': professores})

def atualizarTurma(request):
    if request.method == 'POST':
        form = frmTurmaAtualizar(request.POST)
        if form.is_valid():
            
            cd = form.cleaned_data
            
            codigo = request.POST.get('codigoTurma')

            turma = Turma.objects.get(pk=codigo)
            
            matriculaProfessor = cd['professor']
            professor = Professor.objects.get(pk=matriculaProfessor)
            
            turma.serie = cd['serie']
            turma.sala = cd['sala']
            turma.horaInicial = cd['horaInicial']
            turma.horaFinal = cd['horaFinal']
            turma.professor = professor
            
            turma.save()    

    turmas = Turma.objects.all()           
    return render(request, 'turmas/listar.html', {
        'turmas': turmas
    })