# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

# Models
from portafolio.models import Portafolio

# Permissions
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsStandardUser

# Serializers
from portafolio.serializers import (PortafolioModelSerializer, PortafolioSerializer)


class PortafolioViewSet(mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        viewsets.GenericViewSet):

    serializer_class = PortafolioModelSerializer

    def get_permissions(self): #Acá especificamos qué permisos debe tener el usuario para usar esta VISTA
        permission_classes = [IsAuthenticated, IsStandardUser]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = PortafolioSerializer(data=request.data, context={"request": self.request})
        serializer.is_valid(raise_exception=True)
        por = serializer.save()
        data = PortafolioModelSerializer(por).data
        return Response(data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        """Filtra por usuario autenticado."""
        queryset = Portafolio.objects.filter(user=self.request.user)
        return queryset
