from django.db import models

class Usuario(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20)  

    class Meta:
        db_table = 'Trabajadores'
    

class Estacionamiento(models.Model):
    TIPO_USUARIO_CHOICES = [
        ('Visita', 'Visita'),
        ('Residente', 'Residente'),
        ('Externo', 'Externo'),
    ]

    patente = models.CharField(max_length=20, primary_key=True)
    modelo_auto = models.CharField(max_length=50)
    nombre_usuario_id = models.CharField(max_length=50)
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES)
    contacto = models.CharField(max_length=20)

    class Meta:
        db_table = 'Estacionaminto'
