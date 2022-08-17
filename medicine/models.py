from django.db import models
from company.models import Company
from user.models import CustomUser
# Create your models here.

class ChemicalCompound(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_on = models.TimeField(auto_now_add=True)
    created_by = models.ForeignKey(CustomUser, related_name="creater_Chemical", on_delete = models.DO_NOTHING)
    updated_on = models.TimeField(auto_now=True)
    updated_by = models.ForeignKey(CustomUser, related_name="updater_Chemical", on_delete = models.DO_NOTHING, null=True)

    def __str__(self) -> str:
        return self.name

class Medicine(models.Model):
    name = models.CharField(max_length=255, unique=True)
    max_price = models.IntegerField()
    usage = models.CharField(max_length=255, null=True, blank=True)
    dose = models.CharField(max_length=255, null=True, blank=True)
    prescription = models.BooleanField(null=True, blank=True)
    max_selling_quantity = models.CharField(max_length=255, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete = models.PROTECT)
    chemical_compound = models.ForeignKey(ChemicalCompound, on_delete = models.PROTECT)
    created_on = models.TimeField(auto_now_add=True)
    created_by = models.ForeignKey(CustomUser, related_name="creater_medicine", on_delete = models.DO_NOTHING)
    updated_on = models.TimeField(auto_now=True)
    updated_by = models.ForeignKey(CustomUser, related_name="updater_medicine", on_delete = models.DO_NOTHING, null=True)

    def __str__(self) -> str:
        return self.name
