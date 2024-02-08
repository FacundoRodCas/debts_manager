from django.db import models
#from django.contrib.auth.models import User

class Deudores(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fecha = models.DateTimeField(auto_now_add=True)
    deuda_inicial_pesos = models.FloatField()
    deuda_inicial_dolares = models.FloatField()
    intereses_mensuales = models.IntegerField(default=0)
    #usuario = models.ForeignKey()
    def __str__(self):
        return f"{self.nombre} {self.apellido}"