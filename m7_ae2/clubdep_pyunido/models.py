from django.db import models

# Create your models here.
class Socio(models.Model): #modelo para registro de socios
    run = models.CharField(verbose_name="RUN")
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellidos = models.CharField(max_length=100, verbose_name="Apellidos")
    email = models.EmailField(verbose_name="E-mail")
    comuna = models.CharField(verbose_name="Comuna")

    def __str__(self):
        return f"{self.apellidos}, {self.nombre}"
    