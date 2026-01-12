from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from unfold.admin import ModelAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(ModelAdmin):

    list_display = ("email", "role", "is_staff", "is_active", "date_joined")
    list_filter = ("role", "is_staff", "is_active")

    ordering = ("email",)
    search_fields = ("email",)

    fieldsets = (
    ("Role & Permissions", {
        "fields": ("role", "is_staff", "is_active", "is_superuser", "groups", "user_permissions")
    }),
    (None, {
        "fields": ("email", "password")
    }),
    ("Important dates", {
        "fields": ("last_login", "date_joined")
    }),
)

   
