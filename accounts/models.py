from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class AccountManager( BaseUserManager):
    def create_user(self,username,email, password, **other_fields):   # username,email, password, are the fields which a general user should have to basicaaly sign up   && **other_fields represent optional fields
      user=self.model(username=username, email= email, **other_fields)
      user.set_password(password)
      user.save()
      return user

    def create_superuser(self,username,email, password, **other_fields):   # username,email, password, are the fields which a superuser would surely require to create an account
       other_fields.setdefault('is_staff', True)
       other_fields.setdefault('is_superuser', True)
       other_fields.setdefault('is_active', True)

       return self.create_user(username,email, password, **other_fields)


class Profile( AbstractBaseUser, PermissionsMixin):
    name=models.CharField(max_length=20, null=True)
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=10, null=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects= AccountManager()   # This is going to tell django that AccountManager is going to handle sign ups of superuser as well as general user

    USERNAME_FIELD= 'username'  # Must be unique  # This is the field by which django is going to identify superuser while logging in into django admin

    REQUIRED_FIELDS = ['email']    # These are the fields which the superuser has to enter while creating account # Here username and password are by default

    def __str__(self):
        return self.username


