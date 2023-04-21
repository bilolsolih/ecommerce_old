from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['email', 'is_staff', 'is_active']
    list_filter = ['email', 'is_staff', 'is_active']
    fieldsets = (
        (None, {"fields": ("email", "phone_number", "username", "password")}),
        ("Details", {"fields": ("profile_photo", "first_name", "last_name", "gender")}),
        ("Permissions", {"fields": ("is_staff", "is_superuser", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "phone_number", "username", "password1", "password2", "is_staff", "is_superuser",
                "is_active", "groups", "user_permissions"
            )}
         ),
        ("Details", {"fields": ("profile_photo", "first_name", "last_name", "gender")}),
    )
    search_fields = ('email',)
    ordering = ('-created',)


admin.site.register(User, CustomUserAdmin)

# Register your models here.
