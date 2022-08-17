from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.hashers import make_password

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, phone_number, password, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        email = self.normalize_email(email)
        password=make_password(password)
        user = self.model(email=email, phone_number=phone_number, password=password, **extra_fields)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, phone_number, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        email = self.normalize_email(email)
        password=make_password(password)
        user = self.model(email=email, phone_number=phone_number, password=password, **extra_fields)
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=255, unique = True)
    phone_number = models.CharField(max_length = 10)
    username=None
    objects= CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["phone_number"]

    def __str__(self):
        return "{}".format(self.email)



