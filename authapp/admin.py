from django.contrib import admin
from authapp import models

@admin.register(models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "email"]
    ordering = ["-date_joined"]