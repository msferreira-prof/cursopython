from django import forms

class frmProfessorCadastrar(forms.Form):
    nomeProfessor = forms.CharField(max_length=45)  
    titularidade = forms.IntegerField()
    #fotoProfessor = forms.FileField()

class frmProfessorAtualizar(forms.Form):    
    matriculaProfessor = forms.IntegerField
    nomeProfessor = forms.CharField(max_length=45)  
    titularidade = forms.IntegerField()
    #fotoProfessor = forms.FileField()