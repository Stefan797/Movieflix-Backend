from django.shortcuts import render

# Create your views here.

from django.core.cache.backends.base import DEFAULT_TIMEOUT 
from django.views.decorators.cache import cache_page 
from django.conf import settings

CACHE_TTL = getattr(settings, 'CACHETTL', DEFAULT_TIMEOUT)

# CACHE müssen wir noch testen Video 9 Redis Caching
@cache_page(CACHE_TTL)
def show_movie(request):
    print('Movie X is streaming') 


