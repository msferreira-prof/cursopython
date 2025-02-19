from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('listar/', views.listar, name='listar'),
    path('consultar/', views.consultar, name='consultar'),
    path('atualizarAlu/<int:pk>', views.atualizar, name='atualizarAlu'),
    path('cadastrarAluno', views.cadastrarAluno, name='cadastrarAluno'),    
    path('excluir/<int:pk>', views.excluir, name='excluirAluno'),
    path('atualizarAluno', views.atualizarAluno, name='atualizarAluno'),
]
