# Django
from django.contrib import admin
from portafolio.models import Portafolio

# Models
@admin.register(Portafolio)

class PortAdmin(admin.ModelAdmin):
    """Est admin."""

    list_display = ('user','titulo','descripcion') #Columnas de la tabla visibles, first and last name son campos intrínsecos de user
    list_display_links = ('user', 'titulo','descripcion') #Cliqueables

    search_fields = (
        'user',
        'titulo',
    )

    list_filter = (
        'user',
    )
