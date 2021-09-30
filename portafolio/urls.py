"""Portafolio URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from portafolio import views

router = DefaultRouter()
router.register(r'portafolio', views.PortafolioViewSet, basename='portafolio')

urlpatterns = [
    path('', include(router.urls))
]