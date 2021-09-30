from django.db import models
from users.models import User
import datetime


# Create your models here.
class Estudios(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='estudios')
    institucion = models.CharField(max_length=120)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=120)

    class Meta:
        verbose_name = "Estudio"

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} | {self.titulo}'