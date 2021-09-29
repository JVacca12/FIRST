from django.contrib import admin

# Register your models here.
"""User admin classes."""

# Django
from django.contrib import admin

# Models
from users.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """User admin."""

    list_display = ('pk', 'username', 'email','first_name','last_name') #Columnas de la tabla visibles, first and last name son campos intrínsecos de user
    list_display_links = ('pk', 'username', 'email','first_name','last_name') #Cliqueables

    search_fields = (
        'email',
        'username',
        'first_name',
        'last_name',
    )

    list_filter = (
        'is_active',
        'is_staff',
        'date_joined',
        'modified',
    )

    readonly_fields = ('date_joined', 'modified',)