from django.db import models
from datetime import date
import os
# Create your models here.

Category_one = "keepwatching" # weiterschauen
Category_two = "popularatpresent" # Derzeit beliebt
Category_three = "watchagain" # Nochmal anschauen
# Category_four = "mylist" # Meine Liste
Category_five = "any" # gemischtes
Category_six = "nature" # Natur
Category_seven = "vehicles" #  Fahrzeuge
Category_eight = "funny" # Lustiges
Category_nine = "animals" # Tiere
Category_ten = "programming" # programmieren
Category_eleven = "sea" # Meer


CATEGORY_CHOICES = (
    (Category_one, "keepwatching"),
    (Category_two, "popularatpresent"),
    (Category_three, "watchagain"),
    # (Category_four, "mylist"),
    (Category_five, "any"),
    (Category_six, "nature"), # Natur
    (Category_seven, "vehicles"), #  Fahrzeuge
    (Category_eight, "funny"), # Lustiges
    (Category_nine, "animals"), # Tiere
    (Category_ten, "programming"), # programmieren
    (Category_eleven, "sea"), # Meer
)

# Category_mylist_one = "any"
# Category_mylist_two = "mylist" 

# CATEGORY_MYLIST_CHOICES = (
#     (Category_mylist_one, "any"),
#     (Category_mylist_two, "mylist"),
# )
    

class Movie(models.Model):
    created_at = models.DateField(default=date.today)
    search_terms = models.CharField(max_length=80, blank=True, null=True)
    title = models.CharField(max_length=80, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    movie_file = models.FileField(upload_to='movie', blank=True, null=True)
    screenshot = models.ImageField(upload_to='screenshots/', blank=True, null=True)
    movie_time = models.CharField(max_length=80, blank=True, null=True)
    # special_category_mylist = models.CharField(max_length=50, choices=CATEGORY_MYLIST_CHOICES, default="any")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="any")
    category_german = models.CharField(max_length=80, blank=True, null=True)
    likes = models.IntegerField(default=0, blank=True, null=True)
    # is_liked = models.BooleanField(default=False)


    def filename(self):
        return os.path.basename(self.movie_file.name)
    
    def __str__(self):
        return f"({self.id}) {self.title}" # - {self.created_at}
