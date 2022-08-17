from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Company


# Register your models here.
@admin.register(Company)
class WorkExperienceAdmin(ModelAdmin):
    list_display = (
        "id",
        "name",
        "created_on",
    )
    search_fields = ("name",)
