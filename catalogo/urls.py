from django.contrib import admin
from django.urls import path
from .views import home,login_view,cadastro, ver_filmes, adicionar_filme, editar_filme , excluir_filme, pagina_sucesso



urlpatterns = [
    path('',home, name='home'),
    path('login/', login_view, name='login_view'),
    path('cadastro/', cadastro, name='cadastro'),
    path('ver_filmes/', ver_filmes, name='ver_filmes'),
    path('adicionar_filme/', adicionar_filme, name='adicionar_filme'),
    path('editar_filme/', editar_filme, name='editar_filme'),
    path('pagina_sucesso/', pagina_sucesso, name='sucesso'),
    path('excluir_filme/', editar_filme, name='excluir'),
    
]

