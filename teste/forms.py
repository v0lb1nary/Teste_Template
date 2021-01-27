from django import forms
from .models import *

class ClienteForm(forms.ModelForm):
    """Form definition for Cliente."""

    class Meta:
        """Meta definition for Clienteform."""

        model = Cliente
        fields = ('nome','telefone','endereco','data_nascimento')
