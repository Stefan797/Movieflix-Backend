from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
            first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):    
        date_joined         = models.DateTimeField(default=timezone.now) #verbose_name="date joined",
        is_admin            = models.BooleanField(default=False)
        is_active           = models.BooleanField(default=False)
        is_staff            = models.BooleanField(default=False)
        is_superuser        = models.BooleanField(default=False)
        first_name          = models.CharField(max_length=50)
        last_name           = models.CharField(max_length=50)
        password            = models.CharField(max_length=999)
        email               = models.EmailField(_('email address'), unique=True)
        user_name           = models.CharField(max_length=300, unique=True, default='email')

        objects = CustomAccountManager()

        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = ['user_name', 'first_name']

        def __str__(self):
            return self.user_name


#last_login = models.DateTimeField(default=timezone.now) #verbose_name="last login", 

 #   USERNAME_FIELD = 'email'
 #   REQUIRED_FIELDS= ['username']

 #   def __str__(self):
 #   return self.username


#login #forgotpw 

"""   profile_image       = models.ImageField() # rnd bild generieren? oder aus einer auswahl auswählen lassen? """

#pip install markdown       # Markdown support for the browsable API. vllt noch anschauen?
