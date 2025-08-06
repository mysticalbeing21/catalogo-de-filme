from django import forms
from django.contrib.auth.models import User
from models import Perfil, TIPOS_USUARIO

class CadastroForm(forms, ModelForm):
    password=forms.CharField(widget=forms.PasswordInput,label='Senha')

    confirm_password= forms.CharField(widget=forms.PasswordInput,label='Confirmar senha')

    tipo_usuario= forms.CharField(choices=TIPOS_USUARIO, label='tipo de usuario', widget= forms.Select(attrs=('class:form-select')))

    class meta:
        s


