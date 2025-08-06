from django import forms
from django.contrib.auth.models import User
from models import Perfil, TIPOS_USUARIO

class CadastroForm(forms. ModelForms):
    password=forms.CharField(widget=forms.PasswordInput,label='Senha')

    confirm_password= forms.CharField(widget=forms.PasswordInput,label='Confirmar senha')

    tipo_usuario= forms.ChoiceField(choices=TIPOS_USUARIO, label='tipo de usuario', widget= forms.Select(attrs={'class':'form-select'}))
    

    class meta:
        model=User
        fields=['username','email']
        widget={
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }
        


