# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.filters import SearchFilter

# Permissions
from rest_framework.permissions import IsAuthenticated

# Models
from users.models import User

# Serializers
from search.serializers import CurriculumSerializer

# Permissions
from users.permissions import IsRecruiterUser


class SearchViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    filter_backends = SearchFilter
    queryset = User.objects.filter(is_active=True, is_recruiter=False)
    serializer_class = CurriculumSerializer
    search_fields = [
        'city',
        'country',
        'experiencia__empresa',
        'estudios__titulo',
        'portafolio__descripcion',
    ]

    def get_permissions(self):
        permission_classes = [IsAuthenticated, IsRecruiterUser]
        return [permission() for permission in permission_classes]
