from movies.tasks import convert_720p, convert_480p
from .models import Movie
from django.dispatch import receiver
from django.db.models.signals import post_save
from django_rq import enqueue
import django_rq

@receiver(post_save, sender=Movie)
def movie_post_save(sender, instance, created, **kwargs):
    print('movie ist gespeichert')
    if created: 
        print('New object created')
        queue = django_rq.get_queue('default', autocommit=True)
        queue.enqueue(convert_720p, instance.movie_file.path)
        queue.enqueue(convert_480p, instance.movie_file.path)
        # convert480p(instance.movie_file.path)
        # convert_720p(instance.video_file.path)
