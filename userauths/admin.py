from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
import userauths
from core import models
from core.models import User
from import_export.admin import ImportExportModelAdmin

# User = get_user_model()

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
    )

# class CustomUserAdmin(UserAdmin):
#     fieldsets = UserAdmin.fieldsets + (
#         ('Additional information', {
#             'fields': ('title', 'bio'),
#         }),
#     )
#
#
# admin.site.register(User, CustomUserAdmin)


# class UserAdmin(admin.ModelAdmin):
#     list_display = ['username', 'email', 'first_name', 'last_name']


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ["username", "email"]