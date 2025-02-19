from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('listar/', views.listar, name='listar'),
    path('consultar/', views.consultar, name='consultar'),
    path('atualizarTur/<str:pk>', views.atualizar, name='atualizarTur'),
    path('cadastrarTurma', views.cadastrarTurma, name='cadastrarTurma'),
    path('excluir/<str:pk>', views.excluir, name='excluirTurma'),
    path('atualizarTurma', views.atualizarTurma, name='atualizarTurma'),
]
