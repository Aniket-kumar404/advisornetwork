from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.db.models.fields.related import OneToOneField
from .managers import CustomUserManager
from adminapi.models import Advisor


class User(AbstractBaseUser):

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    objects = CustomUserManager()


class BookedCalls(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    advisor_id = models.OneToOneField(
        Advisor, on_delete=models.CASCADE, unique=True)
    booking_time = models.DateTimeField(auto_now_add=True)
