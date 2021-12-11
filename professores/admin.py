from django.contrib import admin
from .models import Titularidade, Professor

# Register your models here.
class TitularidadeAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome')
    list_display_links = ('codigo', 'nome')
    list_filter = ('codigo', 'nome')
    list_per_page = 10
    search_fields = ('codigo', 'nome')

    
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'nome', 'titularidade', 'publicar')
    list_display_links = ('matricula', 'nome', 'titularidade')    
    

admin.site.register(Titularidade, TitularidadeAdmin)
admin.site.register(Professor, ProfessorAdmin)
