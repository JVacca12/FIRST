# Django
from django.contrib import admin
from experiencia.models import Experiencia

# Models
#admin.site.register(Experiencia)

@admin.register(Experiencia)

class ExpAdmin(admin.ModelAdmin):
    """Exp admin."""

    list_display = ('user', 'cargo','empresa') #Columnas de la tabla visibles, first and last name son campos intrínsecos de user
    list_display_links = ('user', 'cargo','empresa') #Cliqueables

    search_fields = (
        'fecha_inicio',
        'fecha_fin',
        'user',
    )

    list_filter = (
        'user',
        'fecha_inicio',
        'empresa',
    )
