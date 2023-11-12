from django.db import models

# Create your models here.


class Equipo(models.Model):
    nombre = models.CharField(max_length=200)
    estadio = models.CharField(max_length=200)


class Liga(models.Model):
    LIGA_CHOICES = [
        ('1', 'Apertura'),
        ('2', 'Clausura'),
    ]
    liga = models.CharField(max_length=20, choices=LIGA_CHOICES)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, null=True)
    partidos_jugados = models.IntegerField(default=0)
    partidos_ganados = models.IntegerField(default=0)
    partidos_perdidos = models.IntegerField(default=0)
    partidos_empatados = models.IntegerField(default=0)
    goles_favor = models.IntegerField(default=0)
    goles_contra = models.IntegerField(default=0)
    goles_diferencia = models.IntegerField(default=0)
    puntos = models.IntegerField(default=0)

