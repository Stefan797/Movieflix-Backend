from django.shortcuts import render
from django.core.cache.backends.base import DEFAULT_TIMEOUT 
from django.views.decorators.cache import cache_page 
from django.conf import settings
from rest_framework import viewsets
from .models import Movie
from .serializers import MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('-id')
    serializer_class = MovieSerializer



CACHE_TTL = getattr(settings, 'CACHETTL', DEFAULT_TIMEOUT)


@cache_page(CACHE_TTL)
def show_movie(request):
    print('Movie X is streaming') 






