from django.db import models

class Usuario(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20)  

    def __str__(self):
        return self.username
