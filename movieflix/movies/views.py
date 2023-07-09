from django.shortcuts import render
from django.core.cache.backends.base import DEFAULT_TIMEOUT 
from django.views.decorators.cache import cache_page 
from django.conf import settings
from rest_framework import viewsets, permissions
from .models import Movie
from .serializers import MovieSerializer
from wsgiref.util import FileWrapper
from django.http import HttpResponse

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('-id')
    serializer_class = MovieSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        
        category = self.request.query_params.get('category')
        if category is not None:
            self.queryset = Movie.objects.filter(category=category)
        return self.queryset

@cache_page(CACHE_TTL)
def show_movie(request, title):
    if request.method == "GET":
        movie = Movie.objects.get(title=title)
        test = movie.movie_file.path
        print(test)
        file = FileWrapper(open(test, 'rb'))
        response = HttpResponse(file, content_type='video/mp4')
        dynamic_response = 'attachment; filename=' + test
        response['Content-Disposition'] = dynamic_response
    return response