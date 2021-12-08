from django import forms

class frmAlunoCadastrar(forms.Form):
    nomeAluno = forms.CharField(max_length=50)  
    turma = forms.CharField(max_length=3)
