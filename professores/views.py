from django.shortcuts import render, redirect
from .models import Professor, Titularidade
from .forms import frmProfessorCadastrar


# Create your views here.
# def index(request):
#     return render(request, 'home.html')

def cadastrar(request):
    titularidades = Titularidade.objects.all()
    return render(request, 'professores/cadastrar.html', {
        'titularidades': titularidades
    })

def listar(request):
    professores = Professor.objects.all()
    return render(request, 'professores/listar.html', {
        'professores': professores
    })
    
def consultar(request):
    return render(request, 'professores/consultar.html')

def cadastrarProf(request):
    if request.method == 'POST':
        form = frmProfessorCadastrar(request.POST)
        if form.is_valid():
            print(form.get('nomeProfessor'))
            print(form.get('titularidade'))
            print(form.get('fotoProfessor'))
    
    return redirect('/')
