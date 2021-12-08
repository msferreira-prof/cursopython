from django.contrib import admin
from professores.models import Professor
from .models import Turma

# Register your models here.
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'serie', 'sala', 'horaInicial', 'horaFinal', 'professor')
    list_display_links = ('codigo', 'serie', 'sala', 'horaInicial', 'horaFinal', 'professor')
    list_filter = ('codigo', 'serie', 'sala', 'horaInicial', 'horaFinal', 'professor')
    list_per_page = 10
    search_fields = ('serie', 'sala', 'horaInicial', 'professor')
   
admin.site.register(Turma, TurmaAdmin)