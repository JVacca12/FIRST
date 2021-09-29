from django.db import models
from users.models import User

# Create your models here.
class Estudios(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    institucion = models.CharField(max_length=120)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField(null=True)
    titulo = models.CharField(max_length=120)
    
    class Meta:
        verbose_name = "Estudio"

    def __str__(self):
        """Return company and first_name and last_name."""
        return f'{self.user.first_name} {self.user.last_name} | {self.titulo}'