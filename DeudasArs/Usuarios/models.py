from django.db import models


class Usuario(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
