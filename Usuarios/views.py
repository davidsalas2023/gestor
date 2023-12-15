
from django.shortcuts import render, redirect
from .models import Usuario
import random
import string


#########################################

def generar_token(length=10):

    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

#Ingreso usuarios######################################################

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
##############################################################





#Usuarios#####################################################

def admin(request, token):

    return render(request, 'Admin/Admin.html')



def administracion(request , token):

    return render(request, 'Administracion/Administration.html')



def estacionamiento(request, token):

    return render(request, 'Estacionamiento/Estacionamiento.html')
#######################################################################