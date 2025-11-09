from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Información adicional', {'fields': ('role', 'cargo')}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Información adicional', {'fields': ('role', 'cargo')}),
    )
    list_display = ('username', 'first_name', 'last_name', 'role', 'cargo', 'is_active')
    list_filter = BaseUserAdmin.list_filter + ('role',)


