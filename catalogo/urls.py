from django.contrib import admin
from django.urls import path
from .views import home,login,cadastro,ver_filmes,adicionar_filme


urlpatterns = [
    path('',home, name='home'),
    path('login/', login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('ver_filmes/', ver_filmes, name='ver_filmes'),
    path('adicionar_filme/', adicionar_filme, name='adicionar_filme'),
    
]

