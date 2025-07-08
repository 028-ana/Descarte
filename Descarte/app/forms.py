from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'senha', 'tipo_usuario']
        widgets = {
            'senha': forms.PasswordInput(),
        }
