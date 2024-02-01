from django.db import models


class Deudores(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fecha = models.DateTimeField()
    deuda_inicial_pesos = models.FloatField()
    deuda_inicial_dolares = models.FloatField()
    
