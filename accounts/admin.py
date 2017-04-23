from django.contrib import admin
from .models import CimeUser
from rest_framework.authtoken.admin import TokenAdmin
from django.contrib.auth.forms import UserChangeForm


TokenAdmin.raw_id_fields = ('user',)


class CimeUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CimeUser

@admin.register(CimeUser)
class CimeUserAdmin(admin.ModelAdmin):
    """
    Administrador de Django para CimeUsers
    """
    # TODO: Hacer una interfaz de administración cercana a UserAdmin
    # https://github.com/django/django/blob/master/django/contrib/auth/admin.py#L42

    form = CimeUserChangeForm
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Información Personal', {'fields': ('name',)}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        ('Fechas', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    list_display = ('email', 'name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email', 'name')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

    def lookup_allowed(self, lookup, value):
        # No se pueden buscar los passwords.
        if lookup.startswith('password'):
            return False
        return super().lookup_allowed(lookup, value)
