# Django REST Framework
from rest_framework import serializers
# Model
from estudios.models import Estudios
import datetime

class EstudiosModelSerializer(serializers.ModelSerializer):
    """Estudios Model Serializer"""

    class Meta:
        """Meta class."""

        model = Estudios
        fields = (
            'pk',
            'institucion',
            'fecha_inicio',
            'fecha_fin',
            'titulo',
        )

class EstudiosSerializer(serializers.Serializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    institucion = serializers.CharField(max_length=120)
    fecha_inicio = serializers.DateTimeField()
    fecha_fin = serializers.DateTimeField()
    titulo = serializers.CharField(max_length=120)

    def validate_titulo(self, value):
        if 'Ingeniero' not in value:
            raise serializers.ValidationError('Estudios deben ser en ingeniería')
        return value

    def create(self, data):
        exp = Estudios.objects.create(**data)
        return exp
