from django.db import models
from user.models import CustomUser

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_on = models.TimeField(auto_now_add=True)
    created_by = models.ForeignKey(CustomUser, related_name="creater", on_delete = models.DO_NOTHING)
    updated_on = models.TimeField(auto_now=True)
    updated_by = models.ForeignKey(CustomUser, related_name="updater", on_delete = models.DO_NOTHING, null=True)

    def __str__(self) -> str:
        return self.name