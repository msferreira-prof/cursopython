from django.contrib import admin
from professores.models import Professor, Titularidade
from turmas.models import Turma
from .models import Aluno

# Register your models here.
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'nome', 'turma')
    list_display_links = ('matricula', 'nome', 'turma')
    list_filter = ('matricula', 'nome', 'turma')
    list_per_page = 10
    search_fields = ('matricula', 'nome', 'turma')
    

admin.site.register(Aluno, AlunoAdmin)
