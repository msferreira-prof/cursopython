from django.urls import path
from . import views

urlpatterns = [
    path('carga/', views.carregar, name='carga'),
]
