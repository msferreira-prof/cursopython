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
        form = frmProfessorCadastrar(request.POST, request.FILES)
        if form.is_valid():
            
            nome = form.cleaned_data.get('nomeProfessor')
            foto = form.cleaned_data.get('fotoProfessor')
            codigo = form.cleaned_data.get('titularidade')
            
            titularidade =  Titularidade(
                                codigo = codigo
            )

            professor = Professor( 
                            nome = nome,
                            foto = foto,
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
        form = frmProfessorAtualizar(request.POST, request.FILES)
        if form.is_valid():
            
            cd = form.cleaned_data

            matricula = request.POST.get('matriculaProfessor')
            professor = Professor.objects.get(pk=matricula)

            nome = form.cleaned_data.get('nomeProfessor')
            foto = form.cleaned_data.get('fotoProfessor')
            removerFoto = form.cleaned_data.get('removerFoto')

            codigoTitularidade = form.cleaned_data.get('titularidade')
            titularidade = Titularidade.objects.get(pk=codigoTitularidade)
            
            # atualiza professor
            professor.titularidade = titularidade
            professor.nome = nome

            # verifica se a foto foi mudada ou deve ser removida
            if removerFoto: 
                professor.foto = None
            elif foto: 
                professor.foto = foto
            
            professor.save()    

    professores = Professor.objects.all()           
    return render(request, 'professores/listar.html', {
        'professores': professores
    })