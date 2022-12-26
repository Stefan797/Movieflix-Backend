from .models import Movie
from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save, sender=Movie)
def movie_post_save(sender, instance, created, **kwargs):
    print('movie ist gespeichert')
    if created: 
        print('New object created')