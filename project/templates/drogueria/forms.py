from django import forms
from Drogueria.models import Medicamento

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100,
                            widget= forms.TextInput(attrs ={'placeholder': 'Busque algo...'}))

class MedicamentoForm(forms.ModelForm):
  class Meta:
    model = Medicamento
    fields = ['nombre', 'codigo', 'droga','precio']