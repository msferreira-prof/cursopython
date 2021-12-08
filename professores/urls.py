from django.conf.urls import url
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('listar/', views.listar, name='listar'),
    path('consultar/', views.consultar, name='consultar'),
    path('cadastrarProfessor', views.cadastrarProfessor, name='cadastrarProfessor')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

