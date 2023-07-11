from django.db import models

# Create your models here.

class NotificationItem(models.Model): 
        title = models.CharField(max_length=200, null=True)   
        recommendation = models.CharField(max_length=100, null=True)
        other = models.CharField(max_length=100, null=True)
        imgpath = models.CharField(max_length=100, null=True)

        def __str__(self):
            return f'({self.id}) {self.title}'