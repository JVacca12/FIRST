"""Experience URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from estudios import views

router = DefaultRouter()
router.register(r'estudios', views.EstudiosViewSet, basename='estudios')

urlpatterns = [
    path('', include(router.urls))
]