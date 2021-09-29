"""Experience URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from experiencia import views

router = DefaultRouter()
router.register(r'experiencia', views.ExperienceViewSet, basename='experiencia')

urlpatterns = [
    path('', include(router.urls))
]