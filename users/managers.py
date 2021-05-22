from django.contrib.auth.base_user import BaseUserManager
from rest_framework.permissions import AllowAny


class CustomUserManager(BaseUserManager):
    permission_classes = [AllowAny]
    def create_user(self, email,name,is_active=True,is_staff=False,is_superuser=False, password=None):
        
        if not email:
            raise ValueError('Email must be set')
        if not password:
            raise ValueError('Password must be set')
        user = self.model(email=self.normalize_email(email))
        user.name = name
        user.set_password(password)
        user.is_active = is_active
        user.is_superuser = is_superuser
        user.is_staff = is_staff
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password=None ):
        user= self.create_user(email, password=password,is_superuser= True,is_staff=True)
        return user