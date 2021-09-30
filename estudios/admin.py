# Django
from django.contrib import admin
from estudios.models import Estudios

# Models

@admin.register(Estudios)

class EstAdmin(admin.ModelAdmin):
    """Est admin."""

    list_display = ('pk','user', 'institucion','titulo', 'fecha_inicio', 'fecha_fin') #Columnas de la tabla visibles, first and last name son campos intrínsecos de user
    list_display_links = ('user', 'institucion','titulo') #Cliqueables

    search_fields = (
        'user',
        'titulo',
    )

    list_filter = (
        'user',
        'fecha_inicio',
        'institucion',
        'titulo',
    )