from django import forms
from .models import Professor

class frmProfessorCadastrar(forms.Form):
    nomeProfessor = forms.CharField(max_length=45)  
    titularidade = forms.IntegerField()
    fotoProfessor = forms.ImageField(required=False)

class frmProfessorAtualizar(forms.Form):    
    matriculaProfessor = forms.IntegerField
    nomeProfessor = forms.CharField(max_length=45)  
    titularidade = forms.IntegerField()
    fotoProfessor = forms.ImageField(required=False)
    removerFoto = forms.BooleanField(required=False)
