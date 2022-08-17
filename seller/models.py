from django.db import models
from user.models import CustomUser


# Create your models here.
class Seller(models.Model):    
    shop_name= models.CharField(max_length=255)
    location = models.CharField(max_length=255, null=True)
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_on = models.TimeField(auto_now_add=True)
    created_by = models.ForeignKey(CustomUser, related_name="creater_seller", on_delete = models.CASCADE)
    updated_on = models.TimeField(auto_now=True)
    updated_by = models.ForeignKey(CustomUser, related_name="updater_seller", on_delete = models.CASCADE, null=True)

    class Meta:
        unique_together=('shop_name', 'user')
  