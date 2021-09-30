# Django REST Framework
from rest_framework import serializers

# Models
from users.models import User
from experiencia.models import Experiencia
from estudios.models import Estudios
from portafolio.models import Portafolio

class ExperienciaCurriculumSerializer(serializers.ModelSerializer):
    """Experiencia Curriculum Model Serializer"""

    class Meta:
        """Meta class."""

        model = Experiencia
        fields = (
            'fecha_inicio',
            'fecha_fin',
            'cargo',
            'empresa',
        )

class EstudiosCurriculumSerializer(serializers.ModelSerializer):
    """Estudios Curr. Model serializer"""

    class Meta:
        """Meta class"""

        model = Estudios
        fields = (
        'fecha_inicio',
        'fecha_fin',
        'institucion',
        'titulo',
        )

class PortafolioCurriculumSerializer(serializers.ModelSerializer):
    """Portafolio Curr. Model serializer"""

    class Meta:
        """Meta class"""

        model = Portafolio
        fields = (
        'fecha_inicio',
        'fecha_fin',
        'descripcion',
        'titulo',
        )

class CurriculumSerializer(serializers.ModelSerializer):

    experiencia = ExperienciaCurriculumSerializer(many=True)
    estudios = EstudiosCurriculumSerializer(many=True)
    portafolio = PortafolioCurriculumSerializer(many=True)

    class Meta: #Para usar los otros serializers, los creamos dentro del serializer principal y añadimos many = True, ya que queremos traer todos los datos de ese usuario. Después solo necesitamos añadirlo en el listado de fields.
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone',
            'city',
            'country',
            'experiencia',
            'estudios',
            'portafolio',
        )