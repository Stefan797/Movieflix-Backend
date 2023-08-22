from movies.tasks import convert_720p, convert_480p
from .models import Movie
from django.dispatch import receiver
from django.db.models.signals import post_save
from django_rq import enqueue
import django_rq
""" Neu """
from django.conf import settings
from rest_framework.authtoken.models import Token



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
""" -- """


@receiver(post_save, sender=Movie)
def movie_post_save(sender, instance, created, **kwargs):
    print('movie ist gespeichert')
    if created: 
        print('New object created')
        queue = django_rq.get_queue('default', autocommit=True)
        queue.enqueue(convert_720p, instance.movie_file.path, timeout=1000)
        queue.enqueue(convert_480p, instance.movie_file.path, timeout=1000)
        # convert480p(instance.movie_file.path)
        # convert_720p(instance.video_file.path)
