from django import forms
from .models import *


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

class FormAdministracion(forms.ModelForm):
    class Meta:
        model = Administracion
        fields = ['rut', 'habitacion', 'nombre_usuario_id', 'tipo_usuario', 'contacto']
        widgets = {
            'rut': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'habitacion': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'nombre_usuario_id': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'tipo_usuario': forms.widgets.Select(attrs={'class': 'form-control'}),
            'contacto': forms.widgets.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'rut': 'Rut',
            'habitacion': 'Habitacion',
            'nombre_usuario_id': 'Nombre del Usuario',
            'tipo_usuario': 'Tipo de Usuario',
            'contacto': 'Contacto',
        }
        label_suffix = ''




class FormFiltroAdministracion(forms.Form):
    rut= forms.CharField(
        label='Buscar Por Rut',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el rut'})
    )

class FormAdmin(forms.ModelForm):
    class Meta:
        model=Usuario
        fields = ['username', 'password', 'tipo']
        widgets = {
            'username': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'password': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.widgets.Select(attrs={'class': 'form-control'}),

        }
        labels = {
            'username': 'Rut',
            'password': 'Password',
            'tipo': 'Tipo de usuario',

        }
        label_suffix = ''




class FormFiltroAdmin(forms.Form):
    username= forms.CharField(
        label='Buscar Persona',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese rut'})
    )


class FormFiltroSoli(forms.Form):
    rut= forms.CharField(
        label='Cargar solicitudes',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese rut'})
    )
