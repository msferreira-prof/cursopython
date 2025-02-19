from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('listar/', views.listar, name='listar'),
    path('consultar/', views.consultar, name='consultar'),
    path('atualizarProf/<int:pk>', views.atualizar, name='atualizarProf'),
    path('cadastrarProfessor', views.cadastrarProfessor, name='cadastrarProfessor'),
    path('excluir/<int:pk>', views.excluir, name='excluirProfessor'),
    path('atualizarProfessor', views.atualizarProfessor, name='atualizarProfessor'),

]

