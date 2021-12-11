from django import forms

class frmAlunoCadastrar(forms.Form):
    nomeAluno = forms.CharField(max_length=50)  
    turma = forms.CharField(max_length=3)

class frmAlunoAtualizar(forms.Form):
    matriculaAluno = forms.IntegerField
    nomeAluno = forms.CharField(max_length=50)  
    turma = forms.CharField(max_length=3)