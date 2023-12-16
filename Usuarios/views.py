
from .forms import FormEstacionamiento,FormFiltroEstacionamiento
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Usuario,Estacionamiento
import random
import string
from xhtml2pdf import pisa
from django.contrib import messages
from django.template.loader import get_template
import xlwt
from io import BytesIO



def generar_token(length=10):

    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def signup(request):
    if request.method == 'POST':
        usuario = request.POST['username']
        contra = request.POST['password']
        tipo = request.POST['tipo']

        Usuario.objects.create(username=usuario, password=contra, tipo=tipo)


    return render(request, 'Signup/Signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        usuario = Usuario.objects.filter(username=username, password=password).first()

        if usuario:

            token = generar_token()
            usuario.token = token
            usuario.save()

            if usuario.tipo == 'estacionamiento':
                return redirect('estacionamiento', token=token)
            elif usuario.tipo == 'administrador':
                return redirect('admin', token=token)
            elif usuario.tipo == 'administracion':
                return redirect('administracion', token=token)

    return render(request, 'registration/Login.html')
def eliminarautosf(request,patente):
    
    producto = Estacionamiento.objects.get(patente=patente)
    producto.delete()
    
    messages.success(request,'Eliminado')
    return redirect('lista',generar_token())



def estacionamiento(request,token):
    form = FormEstacionamiento()
    if request.method == 'POST':
        form = FormEstacionamiento(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Auto agregado')

    data = {'form':form,'titulo':'Ingresar Autos'}
    return render(request,'Estacionamiento/Estacionamiento.html',data)

def listaautos(request, token):
    form = FormFiltroEstacionamiento()

    if request.method == 'POST':
        form = FormFiltroEstacionamiento(request.POST)
        
        if form.is_valid():
            patente = form.cleaned_data.get('patente', '')

            lista_autos = Estacionamiento.objects.all()
            if patente:
                lista_autos = lista_autos.filter(patente__icontains=patente)

            data = {'form': form, 'patente': patente, 'Estacionaminto': lista_autos}
            return render(request, 'Estacionamiento/Datos.html', data)

    data = {'form': form, 'Estacionaminto': None}
    return render(request, 'Estacionamiento/Datos.html', data)



    
def editarautosf(request,patente):
    per = Estacionamiento.objects.get(patente=patente)
    form = FormEstacionamiento(instance=per)
    if request.method == 'POST':
        form = FormEstacionamiento(request.POST,instance=per)
        if form.is_valid():
            form.save()
            return redirect('lista', generar_token())
    data = {'form':form,'titulo':'Modificar Registro'}
    return render (request,'Estacionamiento/Estacionamiento.html',data)
























