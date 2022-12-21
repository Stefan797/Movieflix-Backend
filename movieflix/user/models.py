from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):    
    email               = models.EmailField(max_length=100, unique=True)
    username            = models.CharField(max_length=30, unique=True)
    date_joined         = models.DateTimeField(auto_now_add=True) #verbose_name="date joined",
    last_login          = models.DateTimeField(auto_now=True) #verbose_name="last login", 
    is_admin            = models.BooleanField(default=True)
    is_active           = models.BooleanField(default=True)
    is_staff            = models.BooleanField(default=True)
    is_superuser        = models.BooleanField(default=True)
  
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= ['username']

    def __str__(self):
        return self.username


#login #forgotpw 

"""   profile_image       = models.ImageField() # rnd bild generieren? oder aus einer auswahl auswählen lassen? """

#pip install markdown       # Markdown support for the browsable API. vllt noch anschauen?
