from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='home'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('listar/', views.listar, name='listar'),
    path('consultar/', views.consultar, name='consultar'),
    path('cadastrarProf', views.cadastrarProf, name='cadastrarProf')
]
