from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('listar/', views.listar, name='listar'),
    path('consultar/', views.consultar, name='consultar'),
    path('cadastrarTurma', views.cadastrarTurma, name='cadastrarTurma'),
    path('atualizar/<str:pk>', views.atualizar, name='atualizarTurma'),
    path('excluir/<str:pk>', views.excluir, name='excluirTurma'),

]
