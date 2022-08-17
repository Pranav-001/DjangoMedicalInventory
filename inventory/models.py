from django.db import models
from seller.models import Seller
from medicine.models import Medicine
from user.models import CustomUser

# Create your models here.
class Inventory(models.Model):
    seller = models.ForeignKey(Seller, on_delete = models.CASCADE )
    medicine = models.ForeignKey(Medicine, on_delete = models.PROTECT)
    stock = models.IntegerField()
    shelf_location = models.CharField(max_length=255, blank=True)
    created_on = models.TimeField(auto_now_add=True)
    created_by = models.ForeignKey(CustomUser, related_name="creater_inventory", on_delete = models.DO_NOTHING)
    updated_on = models.TimeField(auto_now=True)
    updated_by = models.ForeignKey(CustomUser, related_name="updater_inventory", on_delete = models.DO_NOTHING, null=True)

    class Meta:
        unique_together = ('seller', 'medicine')
  