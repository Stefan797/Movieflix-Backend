from django.db import models
from datetime import date

# Create your models here.

class Movie(models.Model):
    created_at = models.DateField(default=date.today)
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=500)
    video_file = models.FileField(upload_to='movie', blank=True, null=True)

    # def __str__(self):
    #     return self.title
