from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, username, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, username, first_name, password, **other_fields)

    def create_user(self, email, username, first_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
            first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        
        return user

class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)

        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):    
        date_joined = models.DateTimeField(default=timezone.now) 
        is_admin = models.BooleanField(default=False)
        is_active = models.BooleanField(default=False)
        is_staff  = models.BooleanField(default=False)
        is_superuser = models.BooleanField(default=False)
        first_name = models.CharField(max_length=50, null=True)
        last_name = models.CharField(max_length=50, null=True)
        password = models.CharField(max_length=999, null=True)
        email= models.EmailField(_('email address'), unique=True, null=True)
        username = models.CharField(max_length=300, unique=True, null=True)

        objects = UserManager()

        USERNAME_FIELD = 'email'
        # REQUIRED_FIELDS = ['username', 'first_name']

        def __str__(self):
            return self.username or self.email or self.first_name or self.last_name