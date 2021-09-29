# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

# Models
from experiencia.models import Experiencia

# Permissions
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsStandardUser

# Serializers
from experiencia.serializers import (ExperienciaModelSerializer, ExperienciaSerializer)


class ExperienceViewSet(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        viewsets.GenericViewSet):

    serializer_class = ExperienciaModelSerializer

    def get_permissions(self): #Acá especificamos qué permisos debe tener el usuario para usar esta VISTA
        permission_classes = [IsAuthenticated, IsStandardUser]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = ExperienciaSerializer(data=request.data, context={"request": self.request})
        serializer.is_valid(raise_exception=True)
        exp = serializer.save()
        data = ExperienciaModelSerializer(exp).data
        return Response(data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        """Filtra por usuario autenticado."""
        queryset = Experiencia.objects.filter(user=self.request.user)
        return queryset