from typing import Any
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)



class UserManager(BaseUserManager):
    """ Manager for users"""

    def create_user(self, email, password=None, **kwargs: Any):
        """Create and save a new user"""
        if not email:
            raise ValueError('User must have an email address')
        
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password):
        """Create and save a new user"""

        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

        
      

class User(AbstractBaseUser, PermissionsMixin):
    """Users for the app"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    created_on = models.DateTimeField('Created On', auto_now_add=True)
    last_modified = models.DateTimeField('Last Modified', auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    # change default username user model from username to email
    USERNAME_FIELD = 'email'
