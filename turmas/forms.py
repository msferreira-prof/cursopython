from django import forms

class frmTurmaCadastrar(forms.Form):
    serie = forms.CharField(max_length=45)  
    sala = forms.CharField(max_length=10)
    horaInicial = forms.TimeField()
    horaFinal = forms.TimeField()
    professor = forms.IntegerField()

class frmTurmaAtualizar(forms.Form):
    codigoTurma = forms.CharField(max_length=3)
    serie = forms.CharField(max_length=45)  
    sala = forms.CharField(max_length=10)
    horaInicial = forms.TimeField()
    horaFinal = forms.TimeField()
    professor = forms.IntegerField()