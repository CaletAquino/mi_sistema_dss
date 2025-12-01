from django.db import models

class Registro1(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Registro2(models.Model):
    nombre = models.CharField(max_length=200)
    categoria = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre
