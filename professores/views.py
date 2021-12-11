from django.shortcuts import render, redirect
from .models import Professor, Titularidade
from .forms import frmProfessorAtualizar, frmProfessorCadastrar


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

def excluir(request, pk):
    professor = Professor.objects.get(pk=pk)
    professor.delete()
    return redirect('/professores/listar')

def atualizar(request, pk):
    titularidades = Titularidade.objects.all()
    professor = Professor.objects.get(pk=pk)
    return render(request, 'professores/atualizar.html', 
        {'professor': professor, 'titularidades': titularidades})

def atualizarProfessor(request):
    if request.method == 'POST':
        form = frmProfessorAtualizar(request.POST)
        if form.is_valid():
            
            cd = form.cleaned_data
            
            matricula = request.POST.get('matriculaProfessor')

            professor = Professor.objects.get(pk=matricula)

            codigoTitularidade = cd['titularidade']
            titularidade = Titularidade.objects.get(pk=codigoTitularidade)
            
            professor.titularidade = titularidade

            professor.nome = cd['nomeProfessor']
            
            professor.save()    

    professores = Professor.objects.all()           
    return render(request, 'professores/listar.html', {
        'professores': professores
    })