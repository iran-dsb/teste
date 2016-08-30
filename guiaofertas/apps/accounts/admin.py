from django.contrib import admin

# Register your models here.
from django.contrib.admin.options import StackedInline
from django.contrib.auth.models import Group, Permission

from guiaofertas.apps.accounts.models.CustomUser import CustomUser


class GroupInline(StackedInline):
    model = Group


class PermissionInline(StackedInline):
    model = Permission


class CustomUserAdmin(admin.ModelAdmin):
    fields = ['empresa', 'name', 'email', 'username', 'password', 'is_active', 'is_staff', 'is_superuser', ]
    list_display = ['empresa', 'name', 'email', 'username', 'is_active', 'is_staff', 'is_superuser']
    search_fields = ['empresa', 'name', 'email', 'username', 'is_active', 'is_staff', 'is_superuser']


admin.site.register(CustomUser, CustomUserAdmin)