from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import ChemicalCompound, Medicine


# Register your models here.
@admin.register(ChemicalCompound)
class ChemicalCompoundAdmin(ModelAdmin):
    list_display = (
        "id",
        "name",
        "created_on",
    )
    search_fields = ("name",)


# Register your models here.
@admin.register(Medicine)
class MedicineAdmin(ModelAdmin):
    list_display = (
        "id",
        "name",
        "max_price",
        "usage",
        "dose",
        "prescription",
        "max_selling_quantity",
        "company",
        "chemical_compound",
    )
    search_fields = (
        "name",
        "usage",
        "company__name",
        "chemical_compound__name",
    )
