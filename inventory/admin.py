from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Inventory


# Register your models here.
@admin.register(Inventory)
class InventoryAdmin(ModelAdmin):
    list_display = (
        "id",
        "seller",
        "medicine",
        "stock",
        "shelf_location",
    )
    search_fields = ("seller__shop_name", "medicine__name", "shelf_location")
