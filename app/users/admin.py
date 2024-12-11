from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User

# https://docs.djangoproject.com/en/5.1/topics/auth/customizing/#custom-users-admin-full-example
class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users"""

    ordering = ['id']
    list_display = ['email', 'name']

    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Permissions", {"fields": ["is_active", "is_staff", "is_superuser"]}),
        ("Dates", {"fields": ["last_login", "created_on"]}),

    ]

    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "name", "password1", "password2", 'is_active', 'is_staff', 'is_superuser'],
            },
        ),
    ]

    search_fields = ["email"]
    readonly_fields = ['last_login', 'created_on']

admin.site.register(User, UserAdmin)
