from django import forms
from .models import Estacionamiento


class FormEstacionamiento(forms.ModelForm):
    class Meta:
        model = Estacionamiento
        fields = ['patente', 'modelo_auto', 'nombre_usuario_id', 'tipo_usuario', 'contacto']
        widgets = {
            'patente': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'modelo_auto': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'nombre_usuario_id': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'tipo_usuario': forms.widgets.Select(attrs={'class': 'form-control'}),
            'contacto': forms.widgets.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'patente': 'Patente',
            'modelo_auto': 'Modelo del Auto',
            'nombre_usuario_id': 'Nombre del Usuario',
            'tipo_usuario': 'Tipo de Usuario',
            'contacto': 'Contacto',
        }
        label_suffix = ''




class FormFiltroEstacionamiento(forms.Form):
    patente = forms.CharField(
        label='Buscar Patente',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la patente'})
    )
