from django import forms
from .models import *

class ClienteForm(forms.ModelForm):
    """Form definition for Cliente."""

    class Meta:
        """Meta definition for Clienteform."""

        model = Cliente
        fields = ('nome','telefone','endereco','data_nascimento')

class ModaliadeForm(forms.ModelForm):
    """Form definition for Modaliade."""

    class Meta:
        """Meta definition for Modaliadeform."""

        model = Modaliade
        fields = ('',)

class TerapeuraForm(forms.ModelForm):
    """Form definition for Terapeura."""

    class Meta:
        """Meta definition for Terapeuraform."""

        model = Terapeura
        fields = ('',)
