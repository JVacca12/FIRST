# Django REST Framework
from rest_framework import serializers
# Model
from portafolio.models import Portafolio

class PortafolioModelSerializer(serializers.ModelSerializer):
    """Portafolio Model Serializer"""

    class Meta:
        """Meta class."""

        model = Portafolio
        fields = (
            'pk',
            'fecha_inicio',
            'fecha_fin',
            'titulo',
            'descripcion',
        )

class PortafolioSerializer(serializers.Serializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    fecha_inicio = serializers.DateTimeField()
    fecha_fin = serializers.DateTimeField()
    titulo = serializers.CharField(max_length=120)
    descripcion = serializers.CharField(max_length=500)

    def create(self, data):
        por= Portafolio.objects.create(**data)
        return por