from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import CustomUser


# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(ModelAdmin):
    list_display = (
        "id",
        "email",
        "phone_number",
    )
    search_fields = ("email", "phone_number")
