from django.db import models
from datetime import date
import os
# Create your models here.

Category_one = "keepwatching"
Category_two = "popularatpresent"
Category_three = "watchagain"
Category_four = "mylist"
Category_five = "any"

CATEGORY_CHOICES = (
    (Category_one, "keepwatching"),
    (Category_two, "popularatpresent"),
    (Category_three, "watchagain"),
    (Category_four, "mylist"),
    (Category_five, "any"),
)
    

class Movie(models.Model):
    created_at = models.DateField(default=date.today)
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=500)
    movie_file = models.FileField(upload_to='movie', blank=True, null=True)
    #category = models.CharField(max_length=80, blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="any")


    def filename(self):
        return os.path.basename(self.movie_file.name)
    # def __str__(self):
    #     return self.title
