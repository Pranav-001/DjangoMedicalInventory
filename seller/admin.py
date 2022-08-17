from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Seller


# Register your models here.
@admin.register(Seller)
class SellerAdmin(ModelAdmin):
    list_display = (
        "id",
        "shop_name",
        "location",
        "user",
        "created_on",
    )
    search_fields = ("shop_name", "location", "user__email", "user__phone_number")
