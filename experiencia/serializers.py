# Django REST Framework
from rest_framework import serializers
# Model
from experiencia.models import Experiencia

class ExperienciaModelSerializer(serializers.ModelSerializer):
    """Experience Model Serializer"""

    class Meta:
        """Meta class."""

        model = Experiencia
        fields = (
            'pk',
            'fecha_inicio',
            'fecha_fin',
            'empresa',
            'cargo',
        )

class ExperienciaSerializer(serializers.Serializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    fecha_inicio = serializers.DateTimeField()
    fecha_fin = serializers.DateTimeField(required=False)
    empresa = serializers.CharField(max_length=250)
    cargo = serializers.CharField(max_length=10000)

    def validate(self, data):
        if data['cargo'] != 'Programador backend' or data['cargo'] != 'Programador frontend':
            raise serializers.ValidationError('El cargo difiere de programación')
        return data

    def create(self, data):
        exp = Experiencia.objects.create(**data)
        return exp
