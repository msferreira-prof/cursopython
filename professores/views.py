from django.shortcuts import render, redirect
from .models import Professor, Titularidade
from .forms import frmProfessorCadastrar


# Create your views here.
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

def cadastrarProfessor(request):
    if request.method == 'POST':
        form = frmProfessorCadastrar(request.POST)
        if form.is_valid():
            
            cd = form.cleaned_data
            
            titularidade =  Titularidade(
                                codigo = cd['titularidade']
            )
            
            professor = Professor( 
                            nome = cd['nomeProfessor'],
                            #foto = models.FileField(blank=True, upload_to='fotos')
                            titularidade = titularidade
            )
            
            professor.save()    
            
            return redirect('/professores/cadastrar')
    
    return redirect('/')
