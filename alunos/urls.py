from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('listar/', views.listar, name='listar'),
    path('consultar/', views.consultar, name='consultar'),
    path('cadastrarAluno', views.cadastrarAluno, name='cadastrarAluno')
]
